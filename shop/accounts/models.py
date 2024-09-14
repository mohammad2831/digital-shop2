from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=250, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    username = models.CharField(max_length=200, unique=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'username']

<<<<<<< HEAD
    def __str__(self):
        return self.username



    @property
    def is_staff(self):
        return self.is_admin
=======

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # دسترسی کامل برای ادمین‌ها
        return self.is_admin

    def has_module_perms(self, app_label):
        # دسترسی کامل برای ادمین‌ها به تمام اپلیکیشن‌ها
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin



class AdminLock(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    locked_at = models.DateTimeField(auto_now_add=True)
>>>>>>> c42e347d (atomic transaction)
