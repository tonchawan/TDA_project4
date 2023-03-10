from django import forms
from .models import Accounts, Recives


# Create new Account
class AccountForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = ('account_name', 'account_number', 'balance')

# Create new Recive
class ReciveForm(forms.ModelForm):
    class Meta:
        model = Recives
        fields = ('account', 'insurance_product', 'recive_amount')