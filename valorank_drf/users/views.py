from django.utils.timezone import now
from django.contrib.auth.tokens import default_token_generator
from django.utils.translation import gettext_lazy as _

from rest_framework_simplejwt.views import TokenObtainPairView as RestTokenObtainPairView

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import exceptions

from djoser.views import UserViewSet as DjoserUserViewSet
from djoser.conf import settings

from . import serializers
from .models import User
from .utils import get_user

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class TokenObtainPairView(RestTokenObtainPairView):
    serializer_class = serializers.TokenObtainPairSerializer


class UserViewSet(DjoserUserViewSet):

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = settings.PERMISSIONS.user_create
        elif self.action == "activation":
            self.permission_classes = settings.PERMISSIONS.activation
        elif self.action == "resend_activation":
            self.permission_classes = settings.PERMISSIONS.password_reset
        elif self.action == "list":
            self.permission_classes = settings.PERMISSIONS.user_list
        elif self.action == "reset_password":
            self.permission_classes = settings.PERMISSIONS.password_reset
        elif self.action == "reset_password_confirm":
            self.permission_classes = settings.PERMISSIONS.password_reset_confirm
        elif self.action == "set_password":
            self.permission_classes = settings.PERMISSIONS.set_password
        elif self.action == "set_username":
            self.permission_classes = settings.PERMISSIONS.set_username
        elif self.action == "reset_username":
            self.permission_classes = settings.PERMISSIONS.username_reset
        elif self.action == "reset_username_confirm":
            self.permission_classes = settings.PERMISSIONS.username_reset_confirm
        elif self.action == "destroy" or (
                self.action == "me" and self.request and self.request.method == "DELETE"
        ):
            self.permission_classes = settings.PERMISSIONS.user_delete
        elif self.action == "new_username_confirm":
            self.permission_classes = settings.PERMISSIONS.new_username_confirm
        return super().get_permissions()

    @action(
        ["post"], detail=False, url_path="reset_{}_confirm".format(User.USERNAME_FIELD)
    )
    def reset_username_confirm(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_username = serializer.data["new_" + User.USERNAME_FIELD]

        setattr(serializer.user, 'temporary_email', new_username)
        if hasattr(serializer.user, "last_login"):
            serializer.user.last_login = now()
        serializer.user.save()

        user = serializer.user
        context = {"user": user}
        to = [serializer.user.temporary_email]
        settings.EMAIL.new_email_confirm(self.request, context).send(to)

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        ["post"], detail=False, url_path="new_{}_confirm".format(User.USERNAME_FIELD)
    )
    def new_username_confirm(self, request):

        default_error_messages = {
            'invalid_link': _('This link is not valid'),
        }

        if default_token_generator.check_token(get_user(request.data['uid']), request.data['token']):
            user = get_user(request.data['uid'])
            new_username = user.temporary_email

            setattr(user, User.USERNAME_FIELD, new_username)
            user.temporary_email = None

            if hasattr(user, "last_login"):
                user.last_login = now()
            user.save()

            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            raise exceptions.AuthenticationFailed(
                default_error_messages['invalid_link'],
                'invalid_link',
            )
