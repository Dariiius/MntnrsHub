# Generated by Django 4.0 on 2021-12-09 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]