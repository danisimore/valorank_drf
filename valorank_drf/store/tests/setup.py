from rest_framework.test import APITestCase
from django.core.files import File
import mock
import io
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from store import models
from users.models import User


class StoreSetUp(APITestCase):

    def setUp(self):
        # Mock объект нужен, чтобы имитировать загрузку изображения в поле модели Product
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'test.jpg'  # Файл должен физически существовать (в media)

        # Создаем ранги для товаров
        self.test_base_rank = models.BaseRank.objects.create(title='Test Base Rank')
        self.test_desired_rank = models.DesiredRank.objects.create(title='Test Desired Rank')

        # Создаем суперпользователя
        self.super_user = User.objects.create_superuser('super@user.tst', 'Password!123')
        self.super_user.save()

        # Создаем обычного пользователя
        self.simple_user = User.objects.create_user('simple@user.tst', 'Password!123')
        self.simple_user.save()

        image = io.BytesIO()
        Image.new('RGB', (640, 640)).save(image, 'JPEG')
        image.seek(0)

        image_file = SimpleUploadedFile('image.jpg', image.getvalue())

        self.test_product = models.Product.objects.create(
            title='Test Product',
            base_rank=self.test_base_rank,
            desired_rank=self.test_desired_rank,
            discount=False,
            old_price=None,
            current_price=300,
            execution_time='Не более 3-х дней',
            image=file_mock.name,
            is_bestseller=True
        )

        self.data = {
            'title': 'Test Product',
            'base_rank': self.test_base_rank,
            'desired_rank': self.test_desired_rank,
            'discount': False,
            'old_price': 0,
            'current_price': 300,
            'execution_time': 'Не более 3-х дней',
            'image': image_file,
            'is_bestseller': False
        }
