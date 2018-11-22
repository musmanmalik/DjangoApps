from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', views.ProductList)
router.register('users', views.UserList)
#router.register('signup', views.signup)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/signup', views.signup)
]