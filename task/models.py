from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=64)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    details = models.TextField()
    complete = models.BooleanField(default=False)
    due = models.DateField()
    created =models.DateTimeField(auto_now_add=True)
    