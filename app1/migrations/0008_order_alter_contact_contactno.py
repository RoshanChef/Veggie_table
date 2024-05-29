# Generated by Django 4.2.3 on 2023-08-20 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True, auto_now=True)),
                ('productId', models.CharField(max_length=1000000)),
                ('price', models.CharField(max_length=1000000)),
                ('quantity', models.CharField(max_length=200000)),
                ('userId', models.CharField(max_length=10000)),
                ('paymentMethod', models.CharField(max_length=10000)),
                ('transactionId', models.CharField(max_length=10000)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='contactNo',
            field=models.IntegerField(),
        ),
    ]