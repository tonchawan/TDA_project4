from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")
        return self.create_user(email=email, password=password, **extra_fields)
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100 , null=True)
    first_name = models.CharField(verbose_name='First Name', max_length=200,       null=True)
    last_name = models.CharField(verbose_name='Last Name', max_length=200,        null=True)
    gender = models.BooleanField(null=True)
    date_of_birth = models.DateField(null=True)
    user_Identity = models.BigIntegerField(validators=[RegexValidator(r'^\d{14}$', 'Enter a valid 14 digit account number.')] ,null=True)
    
    object =CustomUserManager()
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.username
