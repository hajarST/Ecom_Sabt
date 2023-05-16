# Generated by Django 4.1.7 on 2023-05-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Scrapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('image', models.CharField(max_length=2000)),
            ],
        ),
        migrations.AlterField(
            model_name='orderr',
            name='total_price',
            field=models.FloatField(),
        ),
    ]