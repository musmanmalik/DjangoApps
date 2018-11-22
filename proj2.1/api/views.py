from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view, permission_classes

from api.serializer import ProductSerializer, SignupSerializer
from product.models import Product


class ProductList(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignupSerializer


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def signup(request):
    if request.method == 'POST':
        print(request.data)
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

