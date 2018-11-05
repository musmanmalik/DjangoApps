# Generated by Django 2.1.2 on 2018-10-19 06:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Price', models.FloatField()),
                ('Description', models.CharField(max_length=300)),
                ('PicUrl', models.FileField(max_length=500, upload_to='')),
                ('UpdatedOn', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TypeName', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Login', models.CharField(max_length=200)),
                ('Name', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
                ('CreatedOn', models.DateTimeField(default=datetime.datetime.now)),
                ('IsActive', models.BooleanField(default=False, null=True)),
                ('PicUrl', models.FileField(max_length=200, upload_to='')),
                ('IsAdmin', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='UpdatedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.User'),
        ),
    ]
