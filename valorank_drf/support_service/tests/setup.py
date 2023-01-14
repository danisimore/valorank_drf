from rest_framework.test import APITestCase
from rest_framework import status

from users.models import User
from support_service.models import Request


class TestSupportService(APITestCase):

    def setUp(self):
        self.support_request = {
            'email': 'test@suppot.req',
            'problem_description': 'Hi! Please help me!'
        }

        self.invalid_support_request = {
            'email': '1@2.r',
            'problem_description': ''
        }

        self.test_request = Request.objects.create(
            email='some@email.com',
            problem_description='some problem'
        )

        self.super_user = User.objects.create_superuser('super@user.test', 'SuperUserPassword')
        self.simple_user = User.objects.create_user('simple@user.test', 'SimpleUserPassword')





