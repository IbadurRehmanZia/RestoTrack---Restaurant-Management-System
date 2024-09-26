"""
URL configuration for inventory_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventory.views import add_category, add_inventory,report_view ,predict_cost, menu_view ,show_category_and_add_product, nav_bar,show_inventory_and_product_and_add_ingredient, menu_and_category_view, by_order, login_view, home_view, view_inventory, restock_inventory
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('addcategory/', add_category, name='add_category'), 
    path('addcategory/addproduct/', show_category_and_add_product, name='show_category_and_add_product'),
    path('addproduct/', show_category_and_add_product, name='show_category_and_add_product'),
    path('addcategory/addingredient/', show_inventory_and_product_and_add_ingredient, name='show_inventory_and_product_and_add_ingredient'),
    path('addingredient/', show_inventory_and_product_and_add_ingredient, name='show_inventory_and_product_and_add_ingredient'),
    path('addingredient/addcategory', add_category, name='add_category'), 
    path('addingredient/addproduct', show_category_and_add_product, name='show_category_and_add_product'), 
    path('addproduct/addcategory/', add_category, name='add_category'),
    path('addinventory/', add_inventory, name='add_inventory'),
    # path('orders/', category_view_in_checkout, name='category_view_in_checkout'),
    path('orders/', menu_and_category_view, name='menu_and_category_view'),
    # path('login/home/orders', menu_and_category_view, name='menu_and_category_view'),
    path('prediction/', predict_cost, name='predict_cost'),
    path('itemorderdisplay/', by_order, name='by_order'),
    path('login/', login_view, name='login_view'),
    path('home/', home_view, name='home_view'),
    path('menuview/', menu_view, name='menu_view'),
    path('navbar/', nav_bar, name='nav_bar'),
    path('login/home/', home_view, name='home_view'),
    path('viewinventory/', view_inventory, name='viewinventory'),
    path('restock_inventory/', restock_inventory, name='restock_inventory'),
   path('report', report_view, name='report'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   
    # Other URL patterns for your project...
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
