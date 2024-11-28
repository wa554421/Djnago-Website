from django.contrib import admin
from waleed.models import ContactModel  # Import the renamed model

# Register your models here.
admin.site.register(ContactModel)  # Register the renamed model