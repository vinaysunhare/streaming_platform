from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('videos.urls')),  # This will route the root URL to your 'videos' app
]
