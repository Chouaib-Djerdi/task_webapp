from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    note = models.CharField(max_length=500)
    
    def __str__(self):
        return f'{self.note}'