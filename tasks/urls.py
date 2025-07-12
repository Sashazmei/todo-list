from django.urls import path
from .views import task_list, create_task, take_task
from .views import register_view


urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', create_task, name='create_task'),
    path('take/<int:task_id>/', take_task, name='take_task'),
    path('register/', register_view, name='register'),
]
