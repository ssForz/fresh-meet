# Generated by Django 2.2.12 on 2022-07-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20220709_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(max_length=30, null=True, verbose_name='E-mail'),
        ),
    ]
