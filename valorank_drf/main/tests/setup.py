import mock

from rest_framework.test import APITestCase

from django.core.files import File

from articles.models import Article, ArticleCategory
from store import models
from users.models import User


class SetUpMainPageDataTest(APITestCase):

    def setUp(self):
        # Mock объект нужен, чтобы имитировать загрузку изображения в поле модели Article
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'test.jpg'  # Файл должен физически существовать (в media)

        # Создаем категорию для статьи
        test_category = ArticleCategory.objects.create(title='Test category')
        test_category.save()

        # Создаем ранги для товаров
        test_base_rank = models.BaseRank.objects.create(title='Test Base Rank')
        test_desired_rank = models.DesiredRank.objects.create(title='Test Desired Rank')

        # Создаем пользователя с полем is_best=False
        not_best_buster = User.objects.create_user('test@email.test', 'TestPassWord!2')
        not_best_buster.is_best = False
        not_best_buster.save()

        # Создаем пользователя с полем is_best=True
        the_best_user = User.objects.create_user('test@email2.test', 'TestPassWord!2')
        the_best_user.is_best = True
        the_best_user.save()

        for i in range(1, 7):
            """Создаем 6 товаров, 3 из которых имеют поле is_bestseller=True"""
            if len(models.Product.objects.all()) < 3:
                models.Product.objects.create(
                    title='Test Product',
                    base_rank=test_base_rank,
                    desired_rank=test_desired_rank,
                    discount=False,
                    old_price=None,
                    current_price=300,
                    execution_time='Не более 3-х дней',
                    image=file_mock.name,
                    is_bestseller=True
                )
            else:
                models.Product.objects.create(
                    title='Test Product',
                    base_rank=test_base_rank,
                    desired_rank=test_desired_rank,
                    discount=False,
                    old_price=None,
                    current_price=300,
                    execution_time='Не более 3-х дней',
                    image=file_mock.name,
                    is_bestseller=False
                )
            """Создаем 6 статей"""
            Article.objects.create(
                title='Test article',
                content='This is the content of the Test article',
                image=file_mock.name,
                video='https://www.youtube.com/embed/9sQH927Y7m4?controls=1',
                category=test_category,
                is_update=True
            )
