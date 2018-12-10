from django.shortcuts import render

# Create your views here.

def home_swagger(request):
    return render(request, 'index.html')
