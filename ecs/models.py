from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = PhoneNumberField()
    email = models.EmailField()
    # Add other fields as needed