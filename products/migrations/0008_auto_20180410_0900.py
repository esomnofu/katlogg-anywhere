# Generated by Django 2.0.3 on 2018-04-10 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20180404_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='product_description',
            field=models.TextField(default='No Description Available'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.TextField(default='No Description Available'),
        ),
    ]