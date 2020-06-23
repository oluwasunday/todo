from django.urls import path
from .views import *

app_name = 'tasks'

urlpatterns = [
	path('', index, name='index'),
	path('update/<str:pk>/', updateTask, name='update'),
	path('delete/<str:pk>/', deleteTask, name='delete'),
]