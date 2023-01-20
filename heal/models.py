from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

# Create class users

class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    user_first_name = models.CharField(max_length=200,default='unknown')
    user_last_name = models.CharField(max_length=200,default='unknown')
    user_Identity = models.BigIntegerField(default=0,validators=[RegexValidator(r'^\d{14}$', 'Enter a valid 14 digit number.')])

#Create class Accounts

class Accounts(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=200)
    account_number = models.BigIntegerField(validators=[RegexValidator(r'^\d{10}$', 'Enter a valid 10 digit account number.')])
    balance = models.DecimalField(max_digits=15, decimal_places=2)


#Create class InsuranceProducts
class InsuranceProducts(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE,default=1)
    product_name = models.CharField(max_length=200,default='unknown')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    coverage = models.CharField(max_length=200)

#Create class Recives
class Recives(models.Model):
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    insurance_product = models.ForeignKey(InsuranceProducts, on_delete=models.CASCADE)
    recive_date = models.DateTimeField()
    recive_amount = models.DecimalField(max_digits=10, decimal_places=2)