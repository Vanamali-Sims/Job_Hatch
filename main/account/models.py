from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField('is_admin',default=False)
    is_candidate = models.BooleanField('is_candidate',default=False)
    is_recruiter = models.BooleanField('is_recruiter',default=False)
    
class Candidate(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    desc =  models.TextField(max_length=600)
    # resume=models.FileField(upload_to='resume/')

class Jobs(models.Model):
	jobtitle=models.CharField(max_length=20)
	companyname=models.CharField(max_length=30)
	experince=models.IntegerField(null=True)
	salary=models.IntegerField(null=True)
	location=models.CharField(max_length=30)
	opening=models.IntegerField(null=True)
	requirment=models.CharField(max_length=10,null=True)