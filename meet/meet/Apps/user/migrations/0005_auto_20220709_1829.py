# Generated by Django 2.2.12 on 2022-07-09 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20220708_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=30, null=True, verbose_name='E-mail'),
        ),
    ]