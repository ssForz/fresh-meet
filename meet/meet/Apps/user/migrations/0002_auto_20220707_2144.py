# Generated by Django 2.2.12 on 2022-07-07 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Office',
            new_name='User',
        ),
    ]