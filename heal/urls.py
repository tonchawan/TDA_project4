from django.urls import path
from . import views

urlpatterns = [
    path('', views.insuranceproducts_view, name='insuranceproducts_view'),
    path('users/', views.users_view, name='users_view'),
    path('accounts/', views.accounts_view, name='accounts_view'),
    path('recives/', views.recives_view, name='recives_view'),
    
    path('user/<int:pk>', views.user_detail, name='user_detail'),
    path('account/<int:pk>', views.account_detail, name='account_detail'),
    path('product/<int:pk>', views.product_detail, name='product_detail'),
    path('recive/<int:pk>', views.recive_detail, name='recive_detail'),

    path('product/<int:product_id>/buy', views.product_buy, name='product_buy'),
    path('account/new', views.account_create, name='account_form'),
    
    path('account/<int:pk>/update', views.account_update, name='account_update'),
    path('recive/<int:pk>/update', views.recive_update, name='recive_update'),

   path('account/<int:pk>/delete', views.account_delete, name='account_delete'),
   path('recive/<int:pk>/delete', views.recive_delete, name='recive_delete'), 



]   