from django.db import models

# Create your models here.
class Userregister(models.Model):
    name = models.CharField(max_length=200) 
    email= models.EmailField() 
    Number = models.IntegerField()
    address = models.TextField()    
    pincode = models.IntegerField(default=0)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Category(models.Model):
    Category_name = models.CharField(max_length=20)
    image = models.ImageField( upload_to='CategoryImage' , blank=True)
    def __str__(self):
        return self.Category_name

class Product(models.Model):
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    Name = models.TextField(max_length=100)
    Quantity = models.IntegerField()
    Discription = models.TextField()
    image = models.ImageField( upload_to='ProductImage' , blank=True)
    Price= models.IntegerField()


class Contact(models.Model):
    Name = models.TextField(max_length=100)
    email= models.EmailField() 
    contactNo = models.IntegerField()
    message = models.TextField()   


class Order(models.Model):
    userId =  models.CharField(max_length=10000)
    productId =  models.CharField(max_length=1000000)
    # price =  models.CharField(max_length=1000000)
    price =  models.IntegerField()
    quantity =  models.CharField(max_length=200000)
    paymentMethod =  models.CharField(max_length=10000)
    transactionId =  models.CharField(max_length=10000)
    Date = models.DateTimeField(auto_created=True,auto_now=True)
    Total = models.IntegerField(default=0)


