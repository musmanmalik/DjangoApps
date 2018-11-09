from django import forms
from django.contrib.auth.models import User
from .models import Product, Comment


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class Test(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Name']


class AddProduct(forms.ModelForm):
    Type = forms.CharField(widget=forms.ChoiceField)

    class Meta:
        model = Product
        fields = ['Name', 'Price', 'Type', 'Description', 'UpdatedBy', 'PicUrl']


class Comment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
