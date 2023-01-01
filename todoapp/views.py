from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Task
from django.views.generic import FormView,ListView,CreateView,DeleteView,UpdateView,DetailView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

class RegisterView(FormView):
    template_name = 'todoapp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('todoapp:list_task')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
            
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('list_task')
        return super(RegisterView, self).get(*args, **kwargs)

class CustomLoginView(LoginView):
    template_name = 'todoapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        #don't forget this !
        return reverse_lazy('todoapp:list_task')
    

class TasksListView(LoginRequiredMixin,ListView):
     model = Task
     context_object_name = 'tasks'

     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context["tasks"] = context['tasks'].filter(user=self.request.user) 
         return context
     


class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todoapp/task.html'


class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    fields  = ['title','description','created']
    success_url = reverse_lazy('todoapp:list_task')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super(TaskCreateView, self).form_valid(form)


class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    success_url = reverse_lazy('todoapp:list_task')
    
class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todoapp:list_task')