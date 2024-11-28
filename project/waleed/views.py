# from django.shortcuts import render,HttpResponse
# from waleed.models import contact

# # Create your views here.
# def home(request):
#     return render (request,'index.html')

# def contact(request):
#     if request.method=="POST":
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         message=request.POST.get('Message')
#         Contact = contact(names=name, emails=email, messages=message)
#         Contact.save()
#     return render(request, 'contact.html')

# def about(request):
#     return render(request,'about.html')

# def singleproductshop(request):
#     return render (request,'singleproduct.html')

# def shop(request):
#     return render (request,'shop.html')

# def cart(request):
#     return render(request, 'cart.html')

from django.shortcuts import render, HttpResponse
from .models import ContactModel  # Import the renamed mode

# Create your views here.
def home(request):
    return render (request,'index.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('Message')
        Contact = ContactModel(names=name, emails=email, messages=message)  # Use ContactModel
        Contact.save()
    return render(request, 'contact.html')

def about(request):
    return render(request,'about.html')

def singleproductshop(request):
    return render (request,'singleproduct.html')

def shop(request):
    return render (request,'shop.html')

def cart(request):
    return render(request, 'cart.html')