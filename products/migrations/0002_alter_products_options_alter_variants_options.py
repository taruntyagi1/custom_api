# Generated by Django 4.1.4 on 2022-12-08 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'products'},
        ),
        migrations.AlterModelOptions(
            name='variants',
            options={'verbose_name_plural': 'Variants'},
        ),
    ]