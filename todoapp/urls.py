from django.urls import path
from .views import TasksListView,TaskCreateView,TaskDeleteView,TaskUpdateView,CustomLoginView,RegisterView,TaskDetailView
from django.contrib.auth.views import LogoutView

app_name = 'todoapp'

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='todoapp:login'),name='logout'),
    path('register/',RegisterView.as_view(),name='register'),

    path('', TasksListView.as_view(), name='list_task'),
    path('task/<int:pk>',TaskDetailView.as_view(),name='detail_task'),
    path('add/',TaskCreateView.as_view(),name='create_task'),
    path('delete/<int:pk>',TaskDeleteView.as_view(),name='delete_task'),
    path('update/<int:pk>',TaskUpdateView.as_view(),name='update_task'),
]
