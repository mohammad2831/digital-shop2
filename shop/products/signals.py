from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Products, ProductLock

@receiver(post_save, sender=Products)
def release_product_lock(sender, instance, **kwargs):
    try:
        # پاک کردن قفل محصول پس از ذخیره‌سازی
        product_lock = ProductLock.objects.get(product=instance)
        product_lock.lock_session = None
        product_lock.lock_timestamp = None
        product_lock.locked_by = None
        product_lock.save()
    except ProductLock.DoesNotExist:
        pass  # اگر قفلی برای این محصول وجود نداشته باشد، خطا نمی‌دهد
