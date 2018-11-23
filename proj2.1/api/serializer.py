from django.contrib.auth.models import User
from django import forms
from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ('url', 'id', 'Name', 'Price', 'Description', 'PicUrl')


class SignupSerializer(serializers.HyperlinkedModelSerializer):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
