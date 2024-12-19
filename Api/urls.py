from django.urls import path
from . import views

urlpatterns = [
    # Users
    path('users', views.UserList.as_view(), name='user'),
    path('users/<int:pk>', views.UserRead.as_view(), name='user-read'),

    # Services
    path('services', views.ServicesList.as_view(), name='service'),

    # Queues
    path('queues', views.QueuesList.as_view(), name='queue'),
    path('queues/<int:pk>', views.QueueRead.as_view(), name='queue-read')
]
