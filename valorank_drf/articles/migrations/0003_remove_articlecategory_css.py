# Generated by Django 4.1.4 on 2023-01-10 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlecategory',
            name='css',
        ),
    ]
