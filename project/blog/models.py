from django.db import models
from django.urls import reverse
import uuid

class Myblog(models.Model):
    title = models.CharField(max_length=100)
    slug  =models.SlugField(max_length=150,blank=True,null=True)
    des=models.TextField()
    lastedit_date = models.DateTimeField(null=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("detail",args=[self.id])
    
class Item(models.Model):
    title=models.CharField(max_length=100)
    des=models.TextField()
    lastedit_date = models.DateTimeField(null=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail',args=[self.id])
    
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

