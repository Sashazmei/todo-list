from django.urls import path
from .views import (
    TaskListCreateAPIView,
    TaskRetrieveUpdateDestroyAPIView,
    TakeTaskAPIView,
    register_view,
    task_list  # 👈 добавили view для главной
)

urlpatterns = [
    path('', task_list, name='task_list'),  # 👈 теперь / ведёт на HTML-шаблон
    path('api/tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),
    path('api/tasks/<int:task_id>/take/', TakeTaskAPIView.as_view(), name='task-take'),
    path('register/', register_view, name='register'),
]
