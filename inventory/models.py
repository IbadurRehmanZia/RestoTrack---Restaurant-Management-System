from django.db import models

class Category(models.Model): 
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    def __str__(self):
        return self.category_name
    

    class Meta:
       app_label = 'inventory'  # Replace 'your_app_name' with the actual name of your app 

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    product_image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    
    def __str__(self):
        return f"Product Name: {self.product_name} Product Image: {self.product_image} Price: {self.price} Category: {self.category}"
    
 

class Inventory(models.Model):
    inventory_name = models.CharField(max_length=255, null=True)
    inventory_id = models.AutoField(primary_key=True)
    availability = models.DecimalField(max_digits=10, decimal_places=2)
    unit_choices = models.CharField(max_length=100)


    def __str__(self):
    
     return f"Inventory Name: {self.inventory_name} Availability: {self.availability} Unit Choices: {self.unit_choices}"
 

class Ingredients(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_choices = models.CharField(max_length=100)

    def __str__(self):
        return f"Product: {self.product} Inventory: {self.inventory} Quantity: {self.quantity} Unit Choices: {self.unit_choices} "
    
  

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField(auto_now_add=True)  # Set a default value
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return f"Order ID: {self.order_id}, Order Date: {self.order_date}, Total Amount: {self.total_amount}, "
    
 

class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order ID: {self.order.order_id}, Product ID: {self.product.product_id}, Quantity: {self.quantity}, Sub-Total: {self.sub_total}"
    
   
