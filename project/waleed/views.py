from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render (request,'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request,'about.html')

def singleproductshop(request):
    return render (request,'singleproduct.html')

def shop(request):
    return render (request,'shop.html')

def cart(request):
    return render(request, 'cart.html')