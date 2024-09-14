from django.db import models
from accounts.models import User
from products.models import Products
from django.core.validators import MaxValueValidator, MinValueValidator

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    discount = models.IntegerField(blank=True, null=True, default=None)

    class Mete:
        ordering = ('paid', '-updated')


    def __str__(self):
        return f'{self.user} - {self.id}'
    
<<<<<<< HEAD

=======
    
>>>>>>> c42e347d (atomic transaction)
    def get_total_price(self):
        total = sum(item.get_cost() for item in self.items.all())
        if self.discount:
            discount_price = (self.discount /100) * total
            return int(total - discount_price)
        return total
<<<<<<< HEAD
=======

>>>>>>> c42e347d (atomic transaction)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)


    def __str__(self) :
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity
<<<<<<< HEAD
=======
    

>>>>>>> c42e347d (atomic transaction)


class Coupon(models.Model):
    code = models.CharField(max_length=30, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(90)])
    active = models.BooleanField(default=False)
    allowed_users = models.ManyToManyField(User, blank=True, related_name='u_coupons')
    allowed_products = models.ManyToManyField(Products, blank=True, related_name='p_coupons')

    def __str__(self):
        return self.code
    


    

class CouponUsage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    used_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'coupon')



