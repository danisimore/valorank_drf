from django.utils.http import urlsafe_base64_decode
from django.core.exceptions import ValidationError

from .models import User

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def get_user(uidb64):
    try:
        # urlsafe_base64_decode() decodes to bytestring
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (
            TypeError,
            ValueError,
            OverflowError,
            ValidationError,
    ):
        user = None
    return user
