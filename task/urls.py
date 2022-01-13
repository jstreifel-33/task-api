from django.urls import path
from .views import *

urlpatterns = [
    path('create/<int:pk>', TaskList.as_view(), name='create_task'),
    path('change/<int:pk>', TaskChange.as_view(), name='change_task'),
]