# Generated by Django 4.1.7 on 2023-05-08 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_scrapp_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product_Scrapp',
        ),
    ]