from django.db import models

# Create your models here.

class Contact_Details(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=10)
    mobile_number=models.CharField(max_length=15)
    address=models.TextField(max_length=500)