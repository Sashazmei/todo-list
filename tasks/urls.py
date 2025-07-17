from django.urls import path
from .views import (
    TaskListCreateAPIView,
    TaskRetrieveUpdateDestroyAPIView,
    TakeTaskAPIView,
    RegisterView,
    TaskListView,
)

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('api/tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),
    path('api/tasks/<int:task_id>/take/', TakeTaskAPIView.as_view(), name='task-take'),
    path('register/', RegisterView.as_view(), name='register'),
]

