# Generated by Django 4.0.1 on 2022-02-22 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_remove_orderproduct_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='item',
            new_name='product',
        ),
    ]