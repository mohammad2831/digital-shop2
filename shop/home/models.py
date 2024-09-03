from django.db import models
from accounts.models import User
from products.models import Products
from .managers import CommentManager



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='pcomments')
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    

    objects = CommentManager()

    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%Y-%m-%d')} to {self.product.slug}-{self.product.user.username}"