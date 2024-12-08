from django.urls import path
from . import views  # Import your views module

urlpatterns = [
    path('', views.index, name='index'),  # Matches the root URL of the 'videos' app and calls the index view
]
