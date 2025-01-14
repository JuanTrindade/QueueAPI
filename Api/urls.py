from django.urls import path
from . import views

urlpatterns = [
    # Test
    # path('task/<str:task_id>', views.TaskRead.as_view(), name='task-read'),
    # path('task', views.TaskSend.as_view(), name='task-send'),

    # Users
    path('users', views.UserList.as_view(), name='users'),
    path('users/<int:pk>', views.UserRead.as_view(), name='users-read'),

    # Services
    path('services', views.ServicesList.as_view(), name='services'),
    path('services/<int:pk>/solicitations', views.ServicesSolicitations.as_view(), name='services-solicitations'),

    # Queues
    path('queues', views.QueuesList.as_view(), name='queues'),
    path('queues/<int:pk>', views.QueueRead.as_view(), name='queues-read')
]
