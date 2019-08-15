from django.db import models

# Create your models here.
from django.urls import reverse


class Visitor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=70)
    organisation = models.CharField(max_length=250, verbose_name="Organization / Institution")
    address = models.TextField()
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Paper(models.Model):
    name = models.CharField(max_length=100,verbose_name='First Name')
    lname = models.CharField(max_length=100,verbose_name='Last Name')
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=70)
    organisation = models.CharField(max_length=250, verbose_name="Organization / Institution")
    department = models.CharField(max_length=250, verbose_name="Department")
    cname = models.CharField(max_length=250, verbose_name="Conference Name",default="International Seminar on Refugees Welfare Policies and the State")
    ccity = models.CharField(max_length=250, verbose_name="Conference City",default="Trivandrum")
    comments = models.TextField()
    file_up = models.FileField('Document', upload_to='documents/%Y/%m/%d',null=True)
    entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

