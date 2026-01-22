from django.shortcuts import render, get_object_or_404
from .models import ChaiType

def home(request):
    chais = ChaiType.objects.all()
    return render(request, 'myapp/index.html', {'chais': chais})

def chai_price(request, id):
    chai = get_object_or_404(ChaiType, id=id)
    return render(request, 'myapp/chai_prices.html', {'chai': chai})
