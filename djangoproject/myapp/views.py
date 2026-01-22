
from django.shortcuts import render
from .models import ChaiType
from django.shortcuts import get_list_or_404,get_object_or_404


def home(request):
    chais = ChaiType.objects.all()
    return render(request, 'index.html', {'chais': chais})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def chai_price(request, id):
    chai = get_object_or_404(ChaiType, id=id)
    return render(request, 'myapp/chai_prices.html', {'chai': chai})

