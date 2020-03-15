from django.http import HttpResponse
from django.shortcuts import render
from .models import Products
# Create your views here.



def product_view(request):

    obj = Products.objects.get(id = 1)
    
    context = {
        'name': obj.title,
        'descrip': obj.descripssion,

    }

    return render(request , '../templates/shop.html', context)