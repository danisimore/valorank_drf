# Generated by Django 4.1.4 on 2022-12-25 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('problem_description', models.TextField(verbose_name='Описание проблемы')),
                ('creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('status', models.CharField(choices=[('W', 'Waiting'), ('P', 'In processing'), ('R', 'Resolved')], default='Waiting', max_length=300)),
                ('mailbox', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.employeemailbox', verbose_name='Обслуживающий специалист')),
            ],
            options={
                'verbose_name': 'Запрос в службу поддержки',
                'verbose_name_plural': 'Запросы в службу поддержки',
            },
        ),
    ]