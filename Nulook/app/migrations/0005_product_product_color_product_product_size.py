# Generated by Django 5.1 on 2024-10-10 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_cart_customer_rename_id_category_category_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_color',
            field=models.CharField(default='colour', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_size',
            field=models.CharField(default='size', max_length=50),
            preserve_default=False,
        ),
    ]
