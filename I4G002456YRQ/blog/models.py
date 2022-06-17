from statistics import mode
from turtle import title
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Post(models.Model):
   title = models.CharField(max_length=200)
   text = models.TextField()
   author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
   created_date = models.DateTimeField(auto_now_add=True)
   published_date = models.DateTimeField(auto_now_add=True)
   
   
   
   


