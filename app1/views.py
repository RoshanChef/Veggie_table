from django.shortcuts import render,redirect
from django.http import HttpResponse
# from app1.models import Category,Userregister , Product , Contact
from app1.models import *


# Create your views here.
def data(request):
    return HttpResponse("<h1>This is my First Page >> </h1>")


def index(request):
    a = Category.objects.all()
    return render(request,"index.html",{'data':a})


def ProductAll(request):
    a = Product.objects.all()
    return render(request,"Product.html" ,{'product':a})

def productFilter(request,id):
    a = Product.objects.filter(Category=id)
    return render(request,"Product.html" ,{'product':a})

def login(request):
    if request.method == "POST":
        email1= request.POST['email']
        psw1= request.POST['password']
        try:
           user = Userregister.objects.get(email=email1,password = psw1)
           if user:
              request.session['email'] = user.email
              request.session['id'] = user.pk
              print(request.session['id'], request.session['email'])
              return redirect("index1")
           else:
              return render(request,"Login.html",{'m':'invalid Email or password '})
        except:
              return render(request,"Login.html",{'m':'invalid Email or password '})

    return render(request,"Login.html")

def logout(request):
   if 'email' in request.session:
    del request.session['email'] 
    del  request.session['id']
    return redirect('login')
   else:
     return redirect('login')

def profile(request):
    if 'email' in request.session:
        user = Userregister.objects.get(email = request.session['email'] )
        return render(request,'profile.html',{'user':user})
    else:
      return redirect('login')
    

def editprofile(request):
    if 'email' in request.session:
      user = Userregister.objects.get(email = request.session['email'] )
      if request.method == "POST":
            name1= request.POST['name']
            Pincode1= request.POST['pincode']
            Phone1= request.POST['phone']
            # psw1= request.POST['oldpassword']
            address1= request.POST['address']

            user.name = name1
            user.pincode = Pincode1
            user.Number = Phone1
            user.address = address1

            if user.name == name1: 
              user.save()
              redirect('password')
            return render(request,'profile.html',{'user':user,'m':'Profile Updated !!'})
      return render(request,'change_profile.html',{'user':user})
    else:
        return redirect('profile')

       
def chpassword(request): 
  if 'email' in request.session:
     user = Userregister.objects.get(email = request.session['email'] )
     if request.method=="POST":
          psw1= request.POST['CreatePassword']
          psw2= request.POST['confirmPassword']
          if psw1 == psw2:
             user.password=psw1
             user.save()
            #  return render(request,'change_profile.html',{'user':user,'m':'password Updated !!'})
             return redirect('editprofile')
     return render(request,'password.html',{'user':user})
  else:
    return redirect('profile')

def productget(request,id):
      a = Product.objects.get(id=id)
      return render(request,"Product_Details.html",{'data':a})



import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

def buynow(request):
   if 'email' in request.session:
     if request.method == 'POST':
          model = Order()
          # model.userId = str(request.session['id'])
          # request.session['userid']=a.pk
          request.session['productid'] = request.POST['productId']
          productdata = Product.objects.get(id= request.POST['productId'])
          request.session['quantity']="1"
          request.session['price'] = (int(request.session['quantity'] )*productdata.Price)
          request.session['paymentMethod'] = 'Razorpay'
          # request.session['transactionId']=""
          productdata.Quantity-=1
          return redirect('razorpayView') 
   else:
      return redirect('login')
    
def addCart(request):
     if 'email' in request.session:
       orderdata = Order.objects.filter(userId = request.session['id'])
       if request.method == 'POST':
          model = Order()
          model.userId = str(request.session['id'])
          model.productId = request.POST['productId']
          model.quantity="1"
          productdata = Product.objects.get(id= request.POST['productId'])
          model.price = (int(model.quantity)*productdata.Price)
          model.paymentMethod = 'Razorpay'
          model.transactionId ="Anbc45622500"
          productdata.Quantity-=1
          model.Total += model.price
          # total = 0
          # for i in orderdata:
          #   total = int (i.quantity) * i.price + orderdata.Total

          # model.Total = total

          productdata.save()
          model.save()
          return redirect('orderCart')
     else:
        return redirect('login')

RAZOR_KEY_ID = 'rzp_test_hMWZoY81Kx8jaw'
RAZOR_KEY_SECRET = 'Cb3S4TNKbfczQ3vGxs53IfOU'
client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))


def razorpayView(request):
    currency = 'INR'
    amount = int(request.session['price'])*100
    # Create a Razorpay Order
    razorpay_order = client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'http://127.0.0.1:8000/paymenthandler/'    
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url    
    return render(request,'razorpayDemo.html',context=context)



@csrf_exempt
def paymenthandler(request):
    # only accept POST request.
    if request.method == "POST":
        try:
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')

            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = client.utility.verify_payment_signature(
                params_dict)
            
            amount = int(request.session['price'])*100  # Rs. 200
            # capture the payemt
            client.payment.capture(payment_id, amount)

            #Order Save Code
            orderModel = Order()
            orderModel.userId=request.session['id']
            orderModel.quantity=request.session['quantity']
            orderModel.productId = request.session['productId']
            # orderModel.userName = request.session['username']
            # orderModel.userEmail = request.session['userEmail']
            # orderModel.userContact = request.session['userContact']
            # orderModel.address = request.session['address']
            orderModel.price = request.session['price']
            orderModel.paymentMethod = request.session['paymentMethod']
            orderModel.transactionId = payment_id
            productdata=Product.objects.get(id=request.session['productId'])
            productdata.quantity=productdata.quantity-int(request.session['quantity'])
            productdata.save()
            orderModel.save()
            del request.session['productid']
            del request.session['quantity']
            # del request.session['userid']
            # del request.session['username']
            # del request.session['userEmail']
            # del request.session['userContact']
            # del request.session['address']
            del request.session['price']
            del request.session['paymentMethod']
            # render success page on successful caputre of payment
            return render(request,"thanks.html")
        except:
            print("Hello")
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        print("Hello1")
       # if other than POST request is made.
        return HttpResponseBadRequest()




def orderCart(request):
     if 'email' in request.session:
        orderdata = Order.objects.filter(userId = request.session['id'])
        productlist=[]
        list = []
        for i in orderdata:
           productdict={}
           dict = {}
           productdata=Product.objects.get(id=i.productId)
           productdict['image'] = productdata.image
           productdict['name'] = productdata.Name
           productdict['quantity'] = i.quantity
           productdict['price'] = i.price
           productdict['date'] = i.Date
           productdict['transactionid'] = i.transactionId
           i.Total += int(i.price)
           dict['Total'] = i.Total
           productlist.append(productdict)
        list.append(dict)
        return render(request,'myorder.html',{"productlist":productlist , "total" : list})
     else:
       return redirect('login')

def register(request):
    if request.method =="POST":
      name1= request.POST['name']
      email1= request.POST['email']
      Pincode1= request.POST['pincode']
      Phone1= request.POST['phone']
      psw1= request.POST['password']
      address1= request.POST['address']

      user = Userregister(name=name1,email=email1 , Number=Phone1,address=address1,pincode=Pincode1,password=psw1)
      data = Userregister.objects.filter(email = email1)

      if len(data) == 0:  
        user.save()
        return redirect('/login')
      else:
        #  if psw1!= psw2:
        #     return render(request,"register.html",{'m':'both password is not matching'})
         return render(request,"register.html",{'m':'These email-Id already exist try anther else Login'})
    
    return render(request,"register.html")
          

def contact(request):
    if (request.method == "POST"):
      
      name1= request.POST['name']
      email1= request.POST['Email']
      Phone1= request.POST['phone']
      message = request.POST['message']

      user = Contact(Name=name1,email=email1 , contactNo=Phone1,message=message)
      data = Userregister.objects.filter(email = email1)
      if len(data) == 0:  
        return render(request,'contact_us.html')
      else:
        user.save()
        return redirect("/thanks")
    
    return render(request,"contact_us.html")

def thanks(request):
    return render(request,"thanks.html")



