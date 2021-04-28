from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    profile_pic_url = models.CharField(max_length=3000)
    phone_number = models.CharField(max_length=20)
    twitter = models.CharField(max_length=300)
    facebook = models.CharField(max_length=300)
    instagram = models.CharField(max_length=200)


