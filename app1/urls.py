from django.urls import path 
from app1.views import *

urlpatterns = [
    path("data/",data),
    path('',index,name="index1"),
    path('product/',ProductAll , name="veggi"),
    path('product-filter/<int:id>/',productFilter),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('editprofile/',editprofile,name='editprofile'),
    path('profile/',profile,name='profile'),
    path('password/',chpassword,name='password'),
    path('buynow/',buynow,name='buy'),
    path('orderCart/',orderCart,name='orderCart'),
    path('addCart/',addCart,name='addCart'),
    path('razorpayView/',razorpayView,name='razorpayView'),
    path('paymenthandler/',paymenthandler,name='paymenthandler'),
    path('productGet/<int:id>/',productget,name="ProductDetails"),
    # path('productGet/<int:id>/',orderSuccessView,name="orderSuccessView"),
    path('register/',register),
    path('thanks/',thanks,name='thanks'),
    path('contact/',contact),

]
