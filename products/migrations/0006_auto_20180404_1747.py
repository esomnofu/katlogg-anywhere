# Generated by Django 2.0.3 on 2018-04-04 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20180323_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='product_color',
            field=models.CharField(default=['Not Available in Colors'], max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='product_price_change_type',
            field=models.CharField(default='Nil', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_color',
            field=models.CharField(default=['Not Available in Colors'], max_length=500),
        ),
    ]