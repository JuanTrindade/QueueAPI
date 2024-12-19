from django.db import models

class User(models.Model):
    name = models.CharField(
        max_length=255, 
        verbose_name='Nome de Usuário', 
        null=False, 
        blank=False
    )


class Services(models.Model):
    SERVICES_TYPES = {
        "NN": None,
        "IPC": "Image Processing",
    }

    name = models.CharField(
        choices=SERVICES_TYPES, 
        null=False,
        blank=False,
        default="NN"
    )

    is_active = models.BooleanField(
        default=False,
        verbose_name='Está Ativo?'
    )


class Queue(models.Model):
    position = models.IntegerField(
        null=False,
        blank=False
    )

    progress_rate = models.FloatField(
        max_length=100,
        verbose_name='Progresso Atual',
        default=1
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Serviço Ativo?'
    )

    user = models.ForeignKey(
        User,
        verbose_name="User ID",
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    service = models.ForeignKey(
        Services,
        verbose_name="Service ID",
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )