# Generated by Django 5.0 on 2024-01-12 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_ordermain_order_address_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordermain',
            options={'ordering': ['-order_created_at']},
        ),
        migrations.AlterField(
            model_name='ordermain',
            name='order_country',
            field=models.CharField(max_length=50),
        ),
    ]
