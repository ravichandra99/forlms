# Generated by Django 3.0.8 on 2020-08-15 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_myuser_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='email',
            field=models.EmailField(default='a@e.com', max_length=50),
        ),
    ]