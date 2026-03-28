# app - models.py file

from django.db import models
from cloudinary.models import CloudinaryField

class User(models.Model):
    name = models.CharField(max_length=30)
    photo = CloudinaryField('image', default='a.png')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name