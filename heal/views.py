from django.shortcuts import render
from .models import Users
# Create your views here.

def users_view(request):
    users = Users.objects.all()
    context = {'users': users}
    return render(request, 'heal/users_view.html', context)