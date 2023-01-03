from django.contrib.auth.tokens import default_token_generator
from templated_mail.mail import BaseEmailMessage

from django.contrib.sites.models import Site

from djoser import utils
from djoser.conf import settings

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


class ActivationEmail(BaseEmailMessage):
    """
    Переопределенный класс отправки письма с подтверждением почты. Используется в users.serializers.py
    для отправки письма с подтверждением, если пользователь с неподтвержденным email пытается
    авторизоваться на сайте.
    """

    template_name = "email/activation.html"

    # Конструктор класса переопределен, чтобы принимать pk и user, которые используется для создания токена и uid
    def __init__(self, pk=None, user=None, request=None, context=None, template_name=None,
                 *args, **kwargs):
        super(BaseEmailMessage, self).__init__(*args, **kwargs)

        self.pk = pk
        self.user = user

        self.request = request
        self.context = {} if context is None else context
        self.html = None

        if template_name is not None:
            self.template_name = template_name

    def get_context_data(self):
        # ActivationEmail can be deleted
        context = super().get_context_data()

        context["uid"] = utils.encode_uid(self.pk)
        context["token"] = default_token_generator.make_token(self.user)
        context["url"] = settings.ACTIVATION_URL.format(**context)
        context['domain'] = Site.objects.get_current().domain
        context['site_name'] = Site.objects.get_current().name
        return context


class NewEmailVerify(BaseEmailMessage):
    template_name = 'new_email_verify.html'

    def get_context_data(self):
        context = super().get_context_data()

        user = context.get("user")
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.NEW_EMAIL_CONFIRM_URL.format(**context)
        return context
