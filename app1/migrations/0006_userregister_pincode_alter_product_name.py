# Generated by Django 4.2.3 on 2023-08-17 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_category_image_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregister',
            name='pincode',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='Name',
            field=models.TextField(max_length=100),
        ),
    ]
