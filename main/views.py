from django.shortcuts import render
from .models import Product

def show_main(request):
    # name = ['Phone1', 'Phone2']  # Tambahkan nama produk yang sesuai
    # price = ['5000000', '6000000']  # Tambahkan harga produk yang sesuai
    # description = ['This is a very good phone', 'This is another good phone']  # Tambahkan deskripsi produk yang sesuai

    # for i in range(len(name)):
    #     if not Product.objects.filter(name=name[i]).exists():
    #         bruh = Product(name=name[i], price=price[i], description=description[i])
    #         bruh.save()

    # temp = Product.objects.all()
    context = {
        "products":[
            {
                "name": "iphone 11",
                "description": "This is a very good phone",
                "price": 5000000,
                "stock": 10,
                "category": "smartphone"
            },
            {
                "name": "iphone 12",
                "description": "This is another good phone",
                "price": 6000000,
                "stock": 10,
                "category": "smartphone"
            },
            {
                "name": "iphone 13",
                "description": "This is another good phone",
                "price": 7000000,
                "stock": 10,
                "category": "smartphone"
                
            }
        ]
    }
    return render(request, 'main.html', context)  