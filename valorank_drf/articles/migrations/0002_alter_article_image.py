# Generated by Django 4.1.4 on 2023-01-10 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='articles', verbose_name='Изображение'),
        ),
    ]
