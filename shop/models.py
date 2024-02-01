from django.db import models

# Create your models here.
class Products(models.Model):
    
    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="Product",default="Default.png")
    
    
    
class Order(models.Model):
    
    def __str__(self):
        return self.name
    
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode =models.CharField(max_length=200)