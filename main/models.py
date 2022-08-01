from django.db.models.aggregates import Count
from django.urls import reverse
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    # useremail = models.CharField(max_length=50)
    # password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

Order_Status = (
    ('Pending','Pending'),
    ('Processed',"Processed"),
    ('Completed','Completed'),
    ('Cancel','Cancel')
)

class Orders(models.Model):
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Order_Date = models.DateTimeField(auto_now_add=True)
    orderStatus = models.CharField(max_length=50,choices=Order_Status, default='Pending')

    def __str__(self):
        return str(self.customerID)

    def getOrderCount(self,id):
        orders = Orders.objects.filter(orderStatus="Processed",customerID=id).values('customerID').annotate(dcount=Count('id'))
        return orders

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return str(self.name)

class Sub_Category(models.Model):
    CategoryID = models.ForeignKey(Category, related_name='subcategoryies', on_delete=models.CASCADE, blank=True, null=True)
    sub_category_name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('VegetablesData', args=[str(self.sub_category_name)])

    def __str__(self):
        return str(self.sub_category_name)


class CountingUnit(models.Model):
    unit = models.CharField(max_length=50)

    def __str__(self):
        return str(self.unit)

class Products(models.Model):
    Sub_Category_ID = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    # countingUnit = models.ForeignKey(CountingUnit,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    product_image = models.ImageField(upload_to='ProductImg')

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])

    def __str__(self):
        return str(self.name)

Status = (
    ('Enable','Enable'),
    ('Disable','Disable'),
)

class transactions(models.Model):
    productID = models.ForeignKey(Products ,on_delete=models.CASCADE)
    AUID = models.ForeignKey(CountingUnit,on_delete=models.CASCADE)
    Description = models.TextField()
    Price = models.FloatField()
    discount_percentage = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=50,choices=Status, default='Enable')

    def get_sale(self):
        selling_price = int(self.Price * (100 - self.discount_percentage) / 100)
        return selling_price

class OrderDetails(models.Model):
    orderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    productID = models.ForeignKey(transactions, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.FloatField()


class ContactUs(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()

class AboutUs(models.Model):
    Address = models.CharField(max_length=200)
    Number = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

class TermAndConditions(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    updated_date = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateField()

class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    updated_date = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateField()
