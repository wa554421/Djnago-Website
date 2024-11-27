from django.contrib import admin
from django.urls import path,include
from waleed import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('shop',views.shop,name='Shop'),
    path('contact',views.contact,name='Contact'),
    path('about',views.about,name='About'),
    path('singleproductshop',views.singleproductshop,name='Single')
    
]