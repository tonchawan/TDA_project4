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

# Edit User
def user_update(request, pk):
    user = User.objects.get(id=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('/', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'heal/user_form.html', {'form': form})

