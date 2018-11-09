from django.contrib.auth.models import User
from django.db import models

class Type(models.Model):
    TypeName = models.CharField(max_length=300)


class Product(models.Model):
    Name = models.CharField(max_length=200)
    Type = models.ForeignKey(Type, on_delete=models.CASCADE)
    Price = models.FloatField()
    Description = models.CharField(max_length=300)
    PicUrl = models.FileField(max_length=500)
    UpdatedOn = models.DateTimeField(null=True)
    UpdatedBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Comment(models.Model):
    product = models.IntegerField(default=0)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.comment


class Rating(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,default=5)
    t_point = models.FloatField(default=0)
    o_points = models.FloatField(default=0)
