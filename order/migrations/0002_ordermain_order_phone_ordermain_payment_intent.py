# Generated by Django 5.0 on 2024-01-14 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermain',
            name='order_phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='ordermain',
            name='payment_intent',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
