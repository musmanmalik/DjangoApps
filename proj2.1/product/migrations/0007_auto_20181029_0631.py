# Generated by Django 2.1.2 on 2018-10-29 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='o_points',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='t_point',
            field=models.FloatField(default=0),
        ),
    ]
