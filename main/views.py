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
                "nama": "Makarim Zufar Prambudyo",
                "npm": "2306241751",
                "kelas": "PBP D",
            }
        ]
    }
    return render(request, 'main.html', context)  