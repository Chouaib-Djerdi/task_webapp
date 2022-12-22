from django.urls import path
from .views import SignUpView
from django.contrib.auth.views import LoginView

app_name = 'accounts'

urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup'),
    path('login/',LoginView.as_view(template_name='registration/login.html',redirect_authenticated_user=True),name='login'),
]
