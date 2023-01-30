from django.shortcuts import render, redirect
from django.contrib.auth import login
from .form import UserForm
from .models import User


# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})


def user_update(request, pk ):
    account = User.objects.get(id=pk)
    if request.method == "POST":
        form = User(request.POST, instance=account)
        if form.is_valid():
            account = form.save()
            return redirect('user_detail', pk =account.pk)
        else:
            form = User(instance= account)
        return render(request, 'account/user_detail.html', {'form':form})
