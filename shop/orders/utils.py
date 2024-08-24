from django.utils import timezone
from .models import Coupon

def add_allowed_user_to_coupon(coupon_code, user):
    try:
        coupon = Coupon.objects.get(code=coupon_code)
        coupon.allowed_users.add(user)
        coupon.save()
        return "User added to coupon successfully."
    except Coupon.DoesNotExist:
        return "Coupon does not exist."

def add_allowed_product_to_coupon(coupon_code, product):
    try:
        coupon = Coupon.objects.get(code=coupon_code)
        coupon.allowed_products.add(product)
        coupon.save()
        return "Product added to coupon successfully."
    except Coupon.DoesNotExist:
        return "Coupon does not exist."
