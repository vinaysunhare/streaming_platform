from django.shortcuts import render

def index(request):
    return render(request, 'videos/index.html')  # Make sure this template file exists
