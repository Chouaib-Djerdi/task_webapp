from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Task
from django.views.generic import TemplateView,ListView,CreateView,DeleteView,UpdateView

# Create your views here.
class TasksListView(ListView):
     model = Task

class TaskCreateView(CreateView):
    model = Task
    fields  = '__all__'
    success_url = reverse_lazy('todoapp:list_task')

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('todoapp:list_task')
    
class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todoapp:list_task')