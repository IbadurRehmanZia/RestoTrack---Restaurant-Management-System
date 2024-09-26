from django.contrib import admin
from .models import Category, Product, Inventory, Ingredients, Order, Item

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Ingredients)
admin.site.register(Order)
admin.site.register(Item)

