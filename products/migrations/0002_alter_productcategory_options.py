# Generated by Django 3.2.23 on 2024-02-11 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
