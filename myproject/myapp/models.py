from ast import Num
from hmac import digest_size
import numbers
from operator import truediv
from pickle import FALSE, TRUE
from tokenize import Name, Number
import uuid
from xml.dom.minidom import Identified
from django.db import models

# Create your models here.

class User(models.Model):
     id= models.IntegerField(primary_key=True,null=False,auto_created=True,unique=True)
     Name = models.CharField(max_length=100,blank=True, null=False)
     family = models.CharField(max_length=150,blank=True,null=False)
     age = models.SmallIntegerField()
     cod = models.PositiveIntegerField(primary_key=False,unique=True,null=False,default='311111111')
def __detail__(self):
           return self.Name()