from rest_framework_simplejwt.serializers import TokenObtainSerializer as RestTokenObtainSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import exceptions

from django.contrib.auth.models import update_last_login
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate

from .email import ActivationEmail
from .models import User


class TokenObtainSerializer(RestTokenObtainSerializer):
    """
    Кастомный класс TokenObtainSerializer. Переопределен для добавления исключения,
    в случае если пользователь с неподтвержденной почтой пытается войти на сайт,
    а также для отправки письма такому пользователю.
    """

    default_error_messages = {
        'no_active_account': _('No active account found with the given credentials'),
        'no_confirmed_email': _('Email has not been confirmed on this account. Activation email has been sent again.')
    }

    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'password': attrs['password'],
        }
        print(self.context['request'])
        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass

        self.user = authenticate(**authenticate_kwargs)

        # Пользователь, который пытается авторизоваться
        user_data = User.objects.all().filter(email=dict(attrs)['email'])
        # Объект класса User
        user_obj = User.objects.get(email=dict(attrs)['email'])
        # Объект класса отправки письма
        re_send_email = ActivationEmail(pk=user_obj.pk, user=user_obj)

        if user_data.filter(is_active=False):
            # Если email не подтвержден, то отправляем письмо и вызываем исключение
            re_send_email.send([dict(attrs)['email']])
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_confirmed_email'],
                'no_confirmed_email',
            )
        elif not api_settings.USER_AUTHENTICATION_RULE(self.user):
            # Если пользователя с введенным email нет в БД, вызываем исключение
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )

        return {}


class TokenObtainPairSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
