from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializer import ProductSerializer, SignupSerializer
from product.models import Product


class ProductList(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignupSerializer

    # def perform_create(self, serializer):  # new
    #     serializer.save(owner=self.request.user)
