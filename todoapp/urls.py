from django.urls import path
from .views import TasksListView,TaskCreateView,TaskDeleteView,TaskUpdateView


app_name = 'todoapp'

urlpatterns = [
    path('home/',TasksListView.as_view(),name='list_task'),
    path('add/',TaskCreateView.as_view(),name='create_task'),
    path('delete/<int:pk>',TaskDeleteView.as_view(),name='delete_task'),
    path('update/<int:pk>',TaskUpdateView.as_view(),name='update_task'),
    
]
