from django.shortcuts import render, redirect
from inventory.forms import CategoryForm, ProductForm, IngredientForm, InventoryForm
from .models import Category, Ingredients, Inventory, Item, Order
from django.forms import modelformset_factory
from .models import Product, Ingredients
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.contrib.auth import authenticate, login
from decimal import Decimal



def add_category(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success_message = "Category Inserted Successfully!"
            form = CategoryForm()  # Reset the form
            return render(request, 'addcategory.html', {'form': form, 'success_message': success_message})
        else:
            # If the form is not valid, re-render the form with errors
            return render(request, 'addcategory.html', {'form': form})
    else:
        # For GET requests, just render the form
        form = CategoryForm()
        return render(request, 'addcategory.html', {'form': form})
    

def add_inventory(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success_message = "Inventory Inserted Successfully!"
            form = InventoryForm()  # Reset the form
            return render(request, 'addinventory.html', {'form': form, 'success_message': success_message})
        else:
            # If the form is not valid, re-render the form with errors
            return render(request, 'addinventory.html', {'form': form})
    else:
        # For GET requests, just render the form
        form = InventoryForm()
        return render(request, 'addinventory.html', {'form': form})

def show_category_and_add_product(request):
    if request.method == 'POST':
        # Handling product addition
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save()  # Save the form to get the product object
            success_message = "Product Inserted Successfully!"
            messages.success(request, success_message)  # Add success message
            product_form = ProductForm()  # Reset the form
        else:
            # If the form is not valid, re-render the form with errors
            messages.error(request, "Error occurred while inserting product.")
    else:
        # For GET requests, just render the forms
        product_form = ProductForm()
    categories = Category.objects.all()  # Fetch all categories
    return render(request, 'addproduct.html', {'product_form': product_form, 'categories': categories})



def show_inventory_and_product_and_add_ingredient(request):
    # Initialize product_form here
    product_form = ProductForm()

    if request.method == 'POST':
        # Handling ingredient addition
        ingredient_form = IngredientForm(request.POST, request.FILES)
        if ingredient_form.is_valid():
            ingredient_form.save()
            success_message = "Ingredient Inserted Successfully!"
            messages.success(request, success_message)  # Add success message
          
        else:
            # If the form is not valid, display errors
            messages.error(request, "Error occurred while inserting ingredient.")
    else:
        # For GET requests, just render the forms
        ingredient_form = IngredientForm()
        
    ingredients = Inventory.objects.all()
    products = Product.objects.all()
    
    return render(request, 'addingredient.html', {'ingredient_form': ingredient_form, 'product_form': product_form, 'ingredients': ingredients, 'products': products})

def by_order(request):
    # Fetch orders and related items
    orders = Order.objects.all()

    order_data = []
    for order in orders:
        items = Item.objects.filter(order=order)
        item_data = []
        for item in items:
            item_data.append({
                'product_name': item.product.product_name,
                'quantity': item.quantity,
                'sub_total': item.sub_total
            })
        order_data.append({
            'order_id': order.order_id,
            'total_amount': order.total_amount,
            'order_date': order.order_date,
            'items': item_data
        })

    context = {
        'orders': order_data
    }

    return render(request, 'itemorderdisplay.html', context)







@csrf_exempt
def menu_and_category_view(request):
    if request.method == 'POST':
        # If it's a POST request, it means it's the checkout action
        data = json.loads(request.body)
        order_date = data.get('order_date')
        total_amount = data.get('total_amount')
        items = data.get('items', [])

        # Create the order
        with transaction.atomic():
            order = Order.objects.create(order_date=order_date, total_amount=total_amount)

            # Create items
            for item_data in items:
                product_id = item_data.get('product_id')
                quantity = item_data.get('quantity')
                sub_total = item_data.get('sub_total')
                product = Product.objects.get(pk=product_id)
                item = Item.objects.create(order=order, product=product, quantity=quantity, sub_total=sub_total)

                # Update inventory availability
                ingredients = Ingredients.objects.filter(product=product)
                for ingredient in ingredients:
                    inventory = ingredient.inventory
                    used_quantity = ingredient.quantity * quantity
                    inventory.availability -= used_quantity
                    inventory.save()

        return JsonResponse({'message': 'Order placed successfully'}, status=201)

    # If it's not a POST request, render the menu and categories
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'orders.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home/')  # Redirect to home page after successful login
        else:
            message = "Invalid credentials!"
            messages.error(request, message)  # Add error message
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')




def home_view(request):
    return render(request, 'home.html')





# def report_view(request):
#     return render(request, 'report2.html')

from django.http import HttpResponseRedirect

def report_view(request):
    # Replace 'path_to_external_html_file' with the actual path to your external HTML file
    return HttpResponseRedirect('file:///C:/Users/Ibad.DESKTOP-VSTA3VQ/Desktop/real%20resto/report2.html')

import os
import csv
import pandas as pd

def predict_cost(request):
    if request.method == 'POST':
        
        CSV_DIRECTORY = 'C://Users//Ibad.DESKTOP-VSTA3VQ//Desktop//fyp real codes//fyp_arima_model_final//forcasted_data_csvs_by_model'
        selected_month = int(request.POST.get('month'))
        selected_year = int(request.POST.get('year'))
        selected_item = request.POST.get('item')

        # Construct the filename based on the selected item
        filename = f'{selected_item}_forecasts.csv'
        filepath = os.path.join(CSV_DIRECTORY, filename)

        # Read the CSV file for the selected item
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            csv_data = list(reader)

        # Extract month and year from the "Date" column
        for row in csv_data:
            row['Month'] = pd.to_datetime(row['Date']).month
            row['Year'] = pd.to_datetime(row['Date']).year

        # Filter the CSV data based on selected month and year
        filtered_data = [row for row in csv_data if int(row['Month']) == selected_month and int(row['Year']) == selected_year]
        print(filtered_data)

        return render(request, 'prediction.html', {'filtered_data': filtered_data})
        
    return render(request, 'prediction.html')

def nav_bar(request):
    return render(request, 'navbar.html')

def view_inventory(request):
    inventories = Inventory.objects.all()
    return render(request, 'viewinventory.html', {'inventories': inventories})




from django.shortcuts import render
from .models import Category, Product, Ingredients

def menu_view(request):
    categories = Category.objects.all()  # Get all categories
    products_by_category = {}  # Dictionary to store products by category

    # Populate the dictionary with products for each category
    for category in categories:
        products = Product.objects.filter(category=category)
        products_by_category[category] = products

    context = {'categories': categories, 'products_by_category': products_by_category}
    return render(request, 'menu2.html', context)



# def menu_view(request):
#      products = Order.objects.all()

#     product_data = []
#     for product in products:
#         ingredients = ingredients.objects.filter(product=product)
#         ingredient_data = []
#         for ingredient in ingredients:
#             ingredient_data.append({
#                 'product_name': ingredient..product_name,
#                 'quantity': item.quantity,
#                 'sub_total': item.sub_total
#             })
#         order_data.append({
#             'order_id': order.order_id,
#             'total_amount': order.total_amount,
#             'order_date': order.order_date,
#             'items': item_data
#         })

#     context = {
#         'orders': order_data
#     }
#     return render(request, 'menu2.html', {'products': products})




# def restock_inventory(request):
#     if request.method == 'POST':
#         inventory_id = request.POST.get('inventory_id')
#         restock_amount = request.POST.get('restock_amount')
#         try:
#             inventory = Inventory.objects.get(pk=inventory_id)
#             # Convert restock_amount to Decimal
#             restock_amount_decimal = Decimal(restock_amount)
#             # Add restock_amount_decimal to availability
#             inventory.availability += restock_amount_decimal
#             inventory.save()
#             return HttpResponse("Inventory restocked successfully.")
#         except Inventory.DoesNotExist:
#             return HttpResponse("Inventory does not exist.")
#     return HttpResponse("Invalid request method.")


# def restock_inventory(request):
#     if request.method == 'POST':
#         inventory_id = request.POST.get('inventory_id')
#         restock_amount = request.POST.get('restock_amount')
#         if inventory_id and restock_amount:
#             try:
#                 inventory = Inventory.objects.get(pk=inventory_id)
#                 inventory.availability += Decimal(restock_amount)
#                 inventory.save()
#                 return HttpResponse("Inventory restocked successfully.")
#             except Inventory.DoesNotExist:
#                 return HttpResponse("Inventory does not exist.")
#         else:
#             return HttpResponse("Invalid data submitted.")
#     return HttpResponse("Invalid request method.")


@csrf_exempt
def restock_inventory(request):
    if request.method == 'POST':
        # Get the inventory_id and restock_amount from the POST data
        inventory_id = request.POST.get('inventory_id')
        restock_amount = request.POST.get('restock_amount')
        try:
            # Retrieve the inventory object
            inventory = Inventory.objects.get(pk=inventory_id)
            # Update the availability based on the restock amount
            inventory.availability += float(restock_amount)
            inventory.save()
            # Return a JSON response with the updated availability
            return JsonResponse({'updated_availability': str(inventory.availability)})
        except Inventory.DoesNotExist:
            # Handle the case where the inventory does not exist
            return JsonResponse({'error': 'Inventory does not exist'}, status=404)
    # Handle the case where the request method is not POST
    return JsonResponse({'error': 'Invalid request method'}, status=405)