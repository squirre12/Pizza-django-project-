from django.contrib import admin
from .models import Pizza, Drink, Product, Ingredients

# Register your models here.

admin.site.register(Pizza)
admin.site.register(Drink)
admin.site.register(Product)
admin.site.register(Ingredients)