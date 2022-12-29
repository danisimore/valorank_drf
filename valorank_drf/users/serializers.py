from rest_framework_simplejwt.serializers import TokenObtainSerializer as RestTokenObtainSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import exceptions

from django.contrib.auth.models import update_last_login
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate

from .models import User




class TokenObtainSerializer(RestTokenObtainSerializer):
    default_error_messages = {
        'no_active_account': _('No active account found with the given credentials'),
        'no_confirmed_email': _('email has not been confirmed on this account')
    }

    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'password': attrs['password'],
        }

        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass

        self.user = authenticate(**authenticate_kwargs)

        # Пользователь, который пытается авторизоваться
        user_data = User.objects.all().filter(email=dict(attrs)['email'])

        if user_data.filter(is_active=False):
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_confirmed_email'],
                'no_confirmed_email',
            )
        elif not api_settings.USER_AUTHENTICATION_RULE(self.user):
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
