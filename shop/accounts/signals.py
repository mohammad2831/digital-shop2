from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.core.exceptions import PermissionDenied
from .models import AdminLock

@receiver(user_logged_in)
def handle_admin_login(sender, request, user, **kwargs):
    if not user.is_superuser:
        return
    
    # چک کردن قفل‌های موجود
    locks = AdminLock.objects.all()
    if locks.exists():
        raise PermissionDenied("Another admin is currently editing. Please wait.")

    # ایجاد قفل جدید
    AdminLock.objects.create(user=user)


@receiver(user_logged_out)
def handle_admin_logout(sender, request, user, **kwargs):
    if user.is_superuser:
        AdminLock.objects.filter(user=user).delete()