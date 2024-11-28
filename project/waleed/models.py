from django.db import models

# Create your models here.
class ContactModel(models.Model):  # Renamed to ContactModel
    names = models.TextField(max_length=120)
    emails = models.EmailField(max_length=100)
    messages = models.TextField(max_length=120) 