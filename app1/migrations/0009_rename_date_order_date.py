# Generated by Django 4.2.3 on 2023-08-20 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_order_alter_contact_contactno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date',
            new_name='Date',
        ),
    ]