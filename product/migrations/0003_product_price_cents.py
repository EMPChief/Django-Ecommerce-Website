# Generated by Django 5.0 on 2024-01-18 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_description_alter_review_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_cents',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=False,
        ),
    ]
