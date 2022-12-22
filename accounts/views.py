from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.views.generic import CreateView

# Create your views here.
class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("accounts:login")
    
