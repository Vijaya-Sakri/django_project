from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html


# Create your models here.s
import datetime
import os

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_details = models.TextField(max_length=100)

    company_address = models.TextField(max_length=100)
    company_email = models.CharField(max_length=100)
    company_number = models.CharField(max_length=100)
    company_image = models.ImageField(upload_to='images/',blank=True,null=True)
    uid = models.ForeignKey(User,on_delete=models.CASCADE,default=None)

# def image_tag(self):
#     return format_html('<img src = "/media/images/{}" />'.format(self.image))


class profile_image(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    image = models.ImageField(upload_to='images/',blank=True,null=True)

class College_User(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    college_contact = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    uid = models.ForeignKey(User,on_delete=models.CASCADE,default=None)

class College_Events(models.Model):
    name = models.CharField(max_length=100)
    schedule = models.DateField(max_length=100)
    eventType = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    image1 = models.ImageField(upload_to='images/',blank=True,null=True)
    image2 = models.ImageField(upload_to='images/',blank=True,null=True)
    image3 =models.ImageField(upload_to='images/',blank=True,null=True)
    cid = models.ForeignKey(College_User,on_delete=models.CASCADE)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone= models.CharField(max_length=13)
    message =models.TextField(max_length=1000)
