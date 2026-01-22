from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    #return HttpResponse("Welcome to homepage !")
    return render(request,'website/index.html')
def about(request):
    return HttpResponse("Welcome to about page !")
def contact(request):
    return HttpResponse("Welcome to contacts !")
