# Generated by Django 5.0 on 2024-01-12 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_ordermain_order_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermain',
            name='order_first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ordermain',
            name='order_last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
