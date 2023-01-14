import io

import mock

from PIL import Image

from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File

from rest_framework.test import APITestCase

from articles.models import Article, ArticleCategory
from users.models import User


class ArticleTests(APITestCase):

    def setUp(self):
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'test.jpg'  # Файл должен физически существовать (в media)

        test_category = ArticleCategory.objects.create(title='Test category')
        test_category.save()

        self.super_user = User.objects.create_superuser('super@user.tst', 'Password!123')
        self.super_user.save()

        self.simple_user = User.objects.create_user('simple@user.tst', 'Password!123')

        image = io.BytesIO()
        Image.new('RGB', (640, 640)).save(image, 'JPEG')
        image.seek(0)

        image_file = SimpleUploadedFile('image.jpg', image.getvalue())

        self.lonely_article = Article.objects.create(
            title='Test article',
            content='This is the content of the Test article',
            image=file_mock.name,
            video='https://www.youtube.com/embed/9sQH927Y7m4?controls=1',
            category=test_category,
            is_update=True
        )

        self.data = {
            'title': 'Creation test',
            'content': 'Content for self.data',
            'image': image_file,
            'video': 'https://www.youtube.com/embed/9sQH927Y7m4?controls=1',
            'category': test_category,
            'is_update': True
        }
