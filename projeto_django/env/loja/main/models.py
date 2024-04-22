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
    
class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=400)
    detail= models.TextField()
    specs= models.TextField()
    price= models.PositiveIntegerFieldField()
    marca= models.ForeignKey(Marca, on_delete=models.CASCADE)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    color= models.ForeignKey(Color, on_delete=models.CASCADE)
    size= models.ForeignKey(Size, on_delete=models.CASCADE)
    status= models.BooleanFieldField(default=True)    
    image= models.ImageField(upload_to='product_images')
    def __str__(self):
        return self.title
    
