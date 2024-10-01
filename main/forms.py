from django.forms import ModelForm
from main.models import Product
from django import forms

CATEGORY_CHOICES = [
    ('Uncategorized', 'Uncategorized'),
    ('Electronics', 'Electronics'),
    ('Books', 'Books'),
    ('Clothing', 'Clothing'),
    ('Home Appliances', 'Home Appliances'),
    ('Toys', 'Toys'),
    ('Furniture', 'Furniture'),
    ('Beauty', 'Beauty'),
    ('Sports', 'Sports'),
    ('Automotive', 'Automotive'),
    ('Groceries', 'Groceries'),
]

class ProductEntry(ModelForm):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    
    class Meta:
        model = Product
        fields = ['name', 'stock', 'category', 'price', 'description','image']