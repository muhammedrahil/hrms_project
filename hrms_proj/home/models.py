from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Branch(models.Model):
    branch=models.CharField(max_length=255)
    def __str__(self):
      return self.branch

class Category(models.Model):
    category=models.CharField(max_length=255)
    def __str__(self):
      return self.category

class Company(models.Model):
    company=models.CharField(max_length=255)
    def __str__(self):
      return self.company

class Employee(models.Model):
    date=models.DateField(default=timezone.now)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    upload_image=models.FileField(upload_to='upload_image')
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    dob=models.DateField(blank=True, null=True)
    email=models.EmailField()
    emp_id=models.CharField(max_length=30)
    uid=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    blood=models.CharField(max_length=20)
    mobail_no=models.IntegerField(blank=True, null=True)
    company=models.ForeignKey(Company,null=True,on_delete=models.SET_NULL)
    catogory=models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    branch=models.ForeignKey(Branch,null=True,on_delete=models.SET_NULL)
    passport_number=models.CharField(max_length=200)
    visa=models.CharField(max_length=255)
    emirates=models.CharField(max_length=255)
    passport_expiry=models.DateField(blank=True, null=True)
    visa_expiry=models.DateField(blank=True, null=True)
    emirates_expiry=models.DateField(blank=True, null=True)
    insurence=models.CharField(max_length=255)
    insurence_expiry=models.DateField(blank=True, null=True)
    insurance_copy=models.FileField(upload_to='insurance_copy')
    passport_copy=models.FileField(upload_to='passport_copy')
    visa_copy=models.FileField(upload_to='visa_copy')
    emirates_copy=models.FileField(upload_to='emirates_copy')
    other_document=models.FileField(upload_to='other_document')
    notification_email=models.EmailField()
    



