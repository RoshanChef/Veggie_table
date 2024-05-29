from django.contrib import admin
from app1.models import Userregister,Category , Product , Contact,Order
# Register your models here.

# if you want to diplay interms of table 
class UserDisplay(admin.ModelAdmin):
    list_display = ["name","email" , "Number","pincode","address","password"]
    list_filter = ["name","email" , "Number","pincode","address","password"]
    search_fields = ['name' , 'Number']

# what to display
admin.site.register(Userregister,UserDisplay)

class CategorDisplay(admin.ModelAdmin ):
    list_display = ['Category_name']
    search_fields = ['Category_name']

admin.site.register(Category,CategorDisplay)

class ProductDisplay(admin.ModelAdmin):
    list_display = ['Category','Name' , 'Quantity','Price','image']
    list_filter = ['Category','Name']
    search_fields = ['Category' , 'Name']
admin.site.register(Product,ProductDisplay)

class UserQueries(admin.ModelAdmin):
    list_display = ['Name','email' , 'contactNo','message']
    list_filter = ['Name','email' , 'contactNo','message']
    search_fields = ['Name','contactNo']
admin.site.register(Contact,UserQueries)

class MyOrder(admin.ModelAdmin):
    list_display = ['productId','price' , 'quantity','userId','paymentMethod','transactionId','Date','Total']
    list_filter = ['productId','price' , 'quantity','userId','paymentMethod','transactionId','Date']
    search_fields = ['userId','','date']
admin.site.register(Order,MyOrder)
