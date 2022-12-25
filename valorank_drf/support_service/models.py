from django.db import models
from users.models import EmployeeMailbox


class Request(models.Model):
    email = models.EmailField()
    problem_description = models.TextField(verbose_name='Описание проблемы')
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    mailbox = models.ForeignKey(
        EmployeeMailbox,
        on_delete=models.PROTECT,
        null=True, blank=True,
        verbose_name='Обслуживающий специалист'
    )

    CHOICES = (
        ('W', 'Waiting'),
        ('P', 'In processing'),
        ('R', 'Resolved')
    )

    status = models.CharField(max_length=300, choices=CHOICES, default='Waiting')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Запрос в службу поддержки'
        verbose_name_plural = 'Запросы в службу поддержки'
