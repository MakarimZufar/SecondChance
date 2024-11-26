from django.forms import ModelForm
from main.models import Product
from django import forms
from django.utils.html import strip_tags

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
        def clean_name(self):
            name = self.cleaned_data["name"]
            return strip_tags(name)
        def clean_stock(self):
            stock = self.cleaned_data["stock"]
            return strip_tags(stock)

        def clean_category(self):
            category = self.cleaned_data["category"]
            return strip_tags(category)

        def clean_price(self):
            price = self.cleaned_data["price"]
            return strip_tags(price)

        def clean_description(self):
            description = self.cleaned_data["description"]
            return strip_tags(description)
