# Generated by Django 5.0.7 on 2024-07-24 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_attribute_productattribute'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image_base64',
            field=models.TextField(blank=True, null=True),
        ),
    ]
