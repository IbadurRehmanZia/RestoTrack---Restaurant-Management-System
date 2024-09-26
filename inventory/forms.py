from django import forms
from .models import Category, Product, Ingredients, Inventory

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'category_image']  # Include any other fields you want to display in the form


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['inventory_name', 'availability', 'unit_choices']  # Include any other fields you want to display in the form


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_id','product_name', 'product_image', 'price', 'category']  # Include any other fields you want to display in the form


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ['product', 'inventory', 'quantity', 'unit_choices']  # Include any other fields you want to display in the form


