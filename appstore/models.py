from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default = 1)
    description = models.CharField(max_length=250, blank=True, null=True, default='')
    image = models.ImageField(upload_to='uploads/product')
    
    def __str__(self):
        return self.name

'''
class Order(models.Model):
    product = models.ForeignKey(Products, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    address = 
    phone = 
    date = 
    status = 

'''