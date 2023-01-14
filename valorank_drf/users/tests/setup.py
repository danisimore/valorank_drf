from users.models import User
from rest_framework.test import APITestCase
from djoser import utils
from django.contrib.auth.tokens import default_token_generator


class TestAuthentication(APITestCase):

    def setUp(self):
        self.valid_user_data = {
            'email': 'test@email.data',
            'password': 'TestPassword',
            're_password': 'TestPassword',
        }

        self.invalid_user_data = {
            'email': '2',
            'password': '1',
            're_password': '2'
        }

        self.test_user = User.objects.create_user('test@email.tst', 'TestPassword')

        self.extra_data = {
            'uid': utils.encode_uid(self.test_user.pk),
            'token': default_token_generator.make_token(self.test_user),
            'new_email': 'test@new.email',
            'new_password': 'TestNewPassword'
        }

