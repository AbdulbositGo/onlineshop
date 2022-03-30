from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None):
        if not email:
            raise ValueError("user must have an email adres")
        if not phone_number:
            raise ValueError("user must have an phone_number")

        user = self.model(
            email = self.normalize_email(email),
            phone_number = phone_number
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, phone_number, password):
        user = self.create_user(email, phone_number, password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save()
        return user

class Accounts(AbstractBaseUser):
    email = models.CharField(max_length=60, unique=True)
    phone_number = models.CharField(max_length=13)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    data_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['phone_number',]

    objects = AccountManager()

    def __str__(self):
        return f"{self.email}({self.phone_number})"

    def has_perm(self, obj):
        return self.is_admin 

    def has_module_perms(self, obj):
        return True