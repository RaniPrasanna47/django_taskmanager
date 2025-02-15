from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add-task/', views.add_task, name='add_task'),
    path('edit-task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('complete-task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
]