# Generated by Django 4.0.3 on 2022-03-25 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='upload',
            new_name='updated',
        ),
    ]
