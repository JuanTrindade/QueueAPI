from celery import shared_task
from . import models

@shared_task
def put_on_queue(service_id, user_id):
    print('Task started, processing...')
    # position, progress_rate, status
    user = models.User.objects.get(pk=user_id)
    service = models.Services.objects.get(pk=service_id)

    queue = models.Queue()

    queue.user = user
    queue.service = service
    queue.position = 1
    queue.status = 'IPG'

    queue.save()

    return str(queue)