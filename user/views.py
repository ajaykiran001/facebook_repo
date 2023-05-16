from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'user/home.html')

def contact(request):
    return render(request,'user/contact.html')

def about(request):
    return render(request,'user/about.html')