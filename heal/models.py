from django.db import models

# Create your models here.

# Create class users

class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)

#Create class Accounts

class Accounts(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    account_number = models.CharField(max_length=200)

#Create class InsuranceProducts
class InsuranceProducts(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

#Create class Recives
class Recives(models.Model):
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    insurance_product = models.ForeignKey(InsuranceProducts, on_delete=models.CASCADE)
    recive_date = models.DateTimeField()
    recive_amount = models.DecimalField(max_digits=10, decimal_places=2)