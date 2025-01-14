from __future__ import absolute_import, unicode_literals
import os
from django.conf import settings

from celery import Celery
# from ..Api.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'QueueApi.settings')

app = Celery('QueueApi', backend='redis')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)