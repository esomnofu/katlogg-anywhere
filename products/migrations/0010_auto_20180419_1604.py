# Generated by Django 2.0.3 on 2018-04-19 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_ratings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratings',
            old_name='movie_name',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='ratings',
            old_name='movie_rating',
            new_name='product_rating',
        ),
    ]