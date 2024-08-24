from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, username, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        if not phone_number:
            raise ValueError('The Phone Number field must be set')
        if not username:
            raise ValueError('The Username field must be set')

        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, username, password=None):
        user = self.create_user(
            email,
            phone_number=phone_number,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    


