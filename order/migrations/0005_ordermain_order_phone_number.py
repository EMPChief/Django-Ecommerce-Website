# Generated by Django 5.0 on 2024-01-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_ordermain_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermain',
            name='order_phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]