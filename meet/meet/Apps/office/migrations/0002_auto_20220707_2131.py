# Generated by Django 2.2.12 on 2022-07-07 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30, verbose_name='E-mail')),
                ('password', models.CharField(max_length=15, verbose_name='Password')),
            ],
        ),
        migrations.DeleteModel(
            name='Office',
        ),
    ]
