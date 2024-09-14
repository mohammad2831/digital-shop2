from django.db import models
from django.utils import timezone
from accounts.models import User


class Category_Type(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ('name' ,)
    
    def __str__(self):
        return self.name
    
class Category_Company(models.Model):
    type = models.ForeignKey(Category_Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    class Meta:
        ordering = ('name' ,)
    
    def __str__(self):
        return self.name


class Products(models.Model):
    type = models.ForeignKey(Category_Type, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category_Company, on_delete=models.CASCADE, )
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    image = models.ImageField(upload_to='products')
    image_base64 = models.TextField(blank=True, null=True)
    description = models.TextField()
    price = models.IntegerField()
    available = models.BooleanField(default= True)
    stock = models.IntegerField(default=0)  
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
<<<<<<< HEAD

=======
    lock_session = models.CharField(max_length=40, null=True, blank=True)
    lock_timestamp = models.DateTimeField(null=True, blank=True)

    def is_available(self):
        return self.stock > 0
    
>>>>>>> c42e347d (atomic transaction)
    class Meta:
        ordering = ('created' ,)
    
    def __str__(self):
        return self.name
    

<<<<<<< HEAD
=======

class ProductLock(models.Model):
    product = models.OneToOneField(Products, on_delete=models.CASCADE)
    lock_session = models.CharField(max_length=40, null=True, blank=True)
    lock_timestamp = models.DateTimeField(null=True, blank=True)
    locked_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def is_locked(self):
        if self.lock_timestamp and (timezone.now() - self.lock_timestamp).total_seconds() > 300:  # به‌عنوان مثال، 5 دقیقه
            return False
        return self.lock_session is not None




>>>>>>> c42e347d (atomic transaction)
class Attribute(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category_Type, related_name='attributes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class ProductAttribute(models.Model):
    product = models.ForeignKey(Products, related_name='product_attributes', on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.product.name} - {self.attribute.name}: {self.value}'
    



class ProductView(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    session_key = models.CharField(max_length=40, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('product', 'ip_address', 'session_key', 'user')
    def __str__(self):
        return self.ip_address