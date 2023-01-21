from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users_view, name='users_view'),
    path('accounts/', views.accounts_view, name='accounts_view'),
    path('insuranceproducts/', views.insuranceproducts_view, name='insuranceproducts_view'),
    path('recives/', views.recives_view, name='recives_view'),
    path('recive/new', views.recive_create, name='recive_form'),
    path('account/new', views.account_create, name='account_form'),




]   