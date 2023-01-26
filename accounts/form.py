from django import forms
from .models import User


# Create new Account
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username', 
            'password', 
            'first_name', 
            'last_name', 
            'gender', 
            'date_of_birth',
            'user_Identity')