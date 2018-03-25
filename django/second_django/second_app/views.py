from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<em>My Second App</em>')

def help(request):
    content_dict = dict(name="huy",age=14)
    return render(request,'second_app/help.html', content_dict)