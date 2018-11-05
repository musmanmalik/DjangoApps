from django.urls import path
from product import views

app_name = 'product'
urlpatterns = [
    #default url
    path('', views.Homeview, name='home'),
    path('login/', views.login1, name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('update/<pk>', views.ProductUpdate.as_view(), name ='updateproduct'),
    path('addproduct/add', views.Addproduct.as_view(), name ='product-add'),
    path('<int:product_id>/', views.Comment1, name='comment'),
    path('logout/',views.logout1, name = 'logout'),
    path('comments/', views.getcomment, name = "comment"),
    path('rate/', views.getrate, name = "rate"),
    path('<int:product_id>', views.sendtofriend, name="send"),

    path('updateprofile/<pk>', views.ProfileUpdate.as_view(), name = 'updateprofile'),
    path('deleteproduct/<pk>', views.ProductDelete.as_view(), name = 'delete')

]
