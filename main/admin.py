from django.contrib import admin
from .models import(
    Customer,
    Orders,
    Category,
    Sub_Category,
    CountingUnit,
    Products,
    transactions,
    OrderDetails,
    ContactUs,
    AboutUs,
    TermAndConditions,
    PrivacyPolicy
)

# Register your models here.

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'address', 'phone']

@admin.register(Orders)
class OrdersModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'customerID', 'Order_Date', 'orderStatus']

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Sub_Category)
class Sub_CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'CategoryID', 'sub_category_name']

@admin.register(CountingUnit)
class CountingUnitModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'unit']

@admin.register(Products)
class ProductsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'Sub_Category_ID', 'name', 'description','product_image']

@admin.register(transactions)
class TransactionsModelAdmin(admin.ModelAdmin):
    list_display =['id','productID','AUID','Description','Price','status','discount_percentage']

@admin.register(OrderDetails)
class OrderDetailsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'orderID', 'productID', 'quantity','price']

@admin.register(ContactUs)
class ContactUsDetailsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstName', 'lastName', 'email','message']

@admin.register(AboutUs)
class AboutUsDetailsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'Address', 'Number', 'email']

@admin.register(TermAndConditions)
class TermAndConditionsDetailsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'updated_date','expire_date']

@admin.register(PrivacyPolicy)
class PrivacyPolicyModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'updated_date','expire_date']