from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello")

def contacts(request):
    return render(request, 'index.html')