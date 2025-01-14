from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # name = models.CharField(
    #     max_length=255, 
    #     verbose_name='Nome de Usuário', 
    #     null=False, 
    #     blank=False
    # )

    username = models.CharField(
        verbose_name='Nome de Usuário',
        max_length=150,
        unique=True,
        blank=False,
        null=False,
        default=False
    )

    password = models.CharField(
        verbose_name='Senha',
        max_length=255,
        blank=False,
        null=False,
        default=False
    )

    email = models.EmailField(
        verbose_name='Endereço de E-mail',
        blank=False,
        default=False
    )


class Services(models.Model):
    SERVICES_TYPES = {
        'NN': None,
        'IPC': 'Image Processing',
    }

    name = models.CharField(
        choices=SERVICES_TYPES, 
        null=False,
        blank=False,
        default='NN'
    )

    is_active = models.BooleanField(
        default=False,
        verbose_name='Está Ativo?'
    )


class Queue(models.Model):
    STATUS_TYPES = {
        'CPT': 'Completed',
        'IPG': 'In Progress',
        'NTS': 'Not Started',
        'FLD': 'Failed'
    }

    status = models.CharField(
        default='CPT',
        verbose_name='Status?',
        null=False,
        blank=False
    )

    position = models.IntegerField(
        null=False,
        blank=False
    )

    progress_rate = models.FloatField(
        max_length=100,
        verbose_name='Progresso Atual',
        default=1
    )

    user = models.ForeignKey(
        User,
        verbose_name='User ID',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    service = models.ForeignKey(
        Services,
        verbose_name='Service ID',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )