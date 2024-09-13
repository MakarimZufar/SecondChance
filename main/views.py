from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers  
from .models import Product
from .forms import ProductEntry

def show_main(request):
    context = {
        "nama": "Makarim Zufar Prambudyo",
        "npm": "2306241751",
        "kelas": "PBP D",
        "products": Product.objects.all()
    }
    return render(request, 'main.html', context)  

def add_product(request):
    if request.method == 'POST':
        form = ProductEntry(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    else:
        form = ProductEntry()
    return render(request, 'add_product.html', {'form': form})

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml') 

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')