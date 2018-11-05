from django.contrib import admin
from .models import User, Product, Type, Comment, Rating

# Register your models here.
admin.site.register(Product)
admin.site.register(Type)
admin.site.register(Comment)
admin.site.register(Rating)