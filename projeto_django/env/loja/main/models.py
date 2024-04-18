from distutils.command.upload import upload 
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=180)
    image= models.ImageField(upload_to='category_images')

    def __str__(self):
        return self.title

class Color(models.Model):
    title = models.CharField(max_length=100)
    Color_codigo= models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Marca(models.Model):
    title = models.CharField(max_length=100)
    image= models.ImageField(upload_to='category_images')
    def __str__(self):
        return self.title
    
class Size(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    
