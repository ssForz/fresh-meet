# Generated by Django 2.2.12 on 2022-07-07 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0002_auto_20220707_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]