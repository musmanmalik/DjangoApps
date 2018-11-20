from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', views.ProductList)
router.register('users', views.UserList)

urlpatterns = [
    path('api/', include(router.urls)),
]