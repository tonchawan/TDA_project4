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


# Show a User detail
def user_detail(request, pk):
    user = Users.objects.get(id=pk)
    return render(request, 'heal/user_detail.html', {'user':user})

# Show a Account detail
def account_detail(request, pk):
    account = Accounts.objects.all()
    return render(request, 'heal/account_detail.html', {'account':account})

# Show a product detail
def product_detail(request, pk):
    product = InsuranceProducts.objects.get(id=pk)
    return render(request, 'heal/product_detail.html', {'product': product})

# Show a recive detail
def recive_detail(request, pk):
    recive = Recives.objects.get(id=pk)
    return render(request, 'heal/recive_detail.html', {'recive':recive })


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
def product_buy(request, product_id):
    if request.method == 'POST':
        form = ReciveForm(request.POST)
        if form.is_valid():
            recive = form.save(commit=False)
            recive.insurance_product_id = product_id
            recive.save()
            return redirect('product_view')
    else:
        form = ReciveForm()
    return render(request, 'heal/recive_form.html', {'form': form})


# Edit Account 
def account_update(request, pk ):
    account = Accounts.objects.get(id=pk)
    if request.method == "POST":
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            account = form.save()
            return redirect('accounts_view', pk =account.pk)
        else:
            form = ReciveForm()
        return render(request, 'heal/account_form.html', {'form':form})

# Edit Recive
def recive_update(request, pk ):
    recive = Recives.objects.get(id=pk)
    if request.method == "POST":
        form = ReciveForm(request.POST, instance=recive)
        if form.is_valid():
            recive = form.save()
            return redirect('recives_view', pk =recive.pk)
        else:
            form = ReciveForm()
        return render(request, 'heal/recive_form.html', {'form':form})


# Deleate Account
def account_delete(request, pk):
    Accounts.objects.get(id=pk).delete()
    return redirect('users_view')

# Deleate Recive
def recive_delete(request, pk):
    Recives.objects.get(id=pk).delete()
    return redirect('heal/recive_view')

