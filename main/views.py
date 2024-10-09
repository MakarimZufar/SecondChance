from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers  
from .models import Product
from .forms import ProductEntry
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.conf.urls import handler404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags



@login_required(login_url='main:login')
def show_main(request):
    context = {
        "nama": request.user.username,
        "npm": "2306241751",
        "kelas": "PBP D",
        "last_login": request.COOKIES.get('last_login')
    }
    return render(request, 'main.html', context)  

def show_my_products(request):
    my_product = Product.objects.filter(user = request.user)
    context = {
        "products": my_product,
    }
    return render(request, 'my_product.html', context)  

def add_product(request):
    if request.method == 'POST':
        form = ProductEntry(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return redirect('main:show_main')
    else:
        form = ProductEntry()
    return render(request, 'add_product.html', {'form': form})

@csrf_exempt
@require_POST
def add_product_by_ajax(request):
    user = request.user
    name = strip_tags(request.POST.get('name'))
    stock = request.POST.get('stock')
    category = request.POST.get('category')
    price = request.POST.get('price')
    description = request.POST.get('description')
    image = request.FILES.get('image')
    new_product = Product(user=user, name=name, stock=stock, category=category, price=price, description=description, image=image)
    new_product.save()
    return HttpResponse(b"Product added successfully", status=201)


def show_xml(request):
    data = Product.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml') 

def show_json_all(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def show_json_user(request):
    data = Product.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def registration(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('main:show_main')
    return render(request, 'registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                response = HttpResponseRedirect(reverse('main:show_main'))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = Product.objects.get(id=id)
    form = ProductEntry(instance=product)
    if request.method == 'POST':
        form = ProductEntry(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))
    return render(request, 'edit_product.html', {'form': form})

def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect ('main:show_main')

def confirm_delete(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'confirm_delete.html', {'product': product})

def page404(request):
    return render(request, '404.html', status=404)
handler404 = page404

def forgot_password(request):
    return HttpResponse("Password cannot be changed. Please contact the administrator.", status=403)

def about(request):
    context = {
        "nama": "Makarim Zufar Prambudyo",
        "npm": "2306241751",
        "kelas": "PBP D"
        }
    return render(request, 'about.html',context)