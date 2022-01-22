from django.db import models

# Create your models here.

class User(models.Model):
     id= models.IntegerField(primary_key=True,null=False,auto_created=True,unique=True)
     Name = models.CharField(max_length=100,blank=True, null=False)
     family = models.CharField(max_length=150,blank=True,null=False)
     age = models.SmallIntegerField()
     cod = models.PositiveIntegerField(primary_key=False,unique=True,null=False,default='311111111')
