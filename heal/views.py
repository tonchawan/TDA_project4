from django.shortcuts import render, redirect
from .models import Users, Accounts, InsuranceProducts, Recives
from .forms import AccountForm, ReciveForm


# Create your views here.

# Show all User data
def users_view(request):
    users = Users.objects.all()
    context = {'users': users}
    return render(request, 'heal/users_view.html', context)

# Show all Accounts data
def accounts_view(request):
    accounts = Accounts.objects.all()
    context = {'accounts': accounts}
    return render(request, 'heal/accounts.html', context)

# Show all insuranceproducts data
def insuranceproducts_view(request):
    insuranceproducts = InsuranceProducts.objects.all()
    context = {'insuranceproducts': insuranceproducts}
    return render(request, 'heal/products.html', context)

# Show all Recives data
def recives_view(request):
    recives = Recives.objects.all()
    context = {'recives': recives}
    return render(request, 'heal/recives.html', context)

# Create Account
def account_create(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save()
            return redirect('accounts_view')
    else:
        form = AccountForm()
    return render(request, 'heal/account_form.html', {'form': form})

#Create recive
def recive_create(request):
    if request.method == 'POST':
        form = ReciveForm(request.POST)
        if form.is_valid():
            recive = form.save()
            return redirect('recives_view')
    else:
        form = ReciveForm()
    return render(request, 'heal/recive_form.html', {'form': form})

