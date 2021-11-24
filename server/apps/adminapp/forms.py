from django import forms
from django.contrib.auth.forms import UserCreationForm

from server.apps.authapp.forms import ShopUserEditForm, ShopUserRegisterForm
from server.apps.authapp.models import ShopUser
from server.apps.geekshop.models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'is_active', 'products']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'is_active', 'price', 'quantity', 'image']


class UserEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = '__all__'


class UserCreateForm(ShopUserRegisterForm):
    pass
