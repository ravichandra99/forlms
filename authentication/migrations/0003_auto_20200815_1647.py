# Generated by Django 3.0.8 on 2020-08-15 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20200814_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='branch',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='college',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='last name'),
        ),
    ]
