from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskList.as_view(), name='create_task'),
    path('<int:pk>', TaskChange.as_view(), name='change_task'),
]