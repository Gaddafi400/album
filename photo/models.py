from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary.forms import CloudinaryFileField
from PIL import Image
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    # image = CloudinaryField('django-upload')
    image = CloudinaryField('django-upload')
    phone_number = models.CharField(max_length=20, blank=True)
    twitter = models.CharField(max_length=300)
    facebook = models.CharField(max_length=300)
    instagram = models.CharField(max_length=200)


