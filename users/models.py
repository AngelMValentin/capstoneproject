from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
User:
first_name
last_name
email
username
password
"""

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=12)