# Generated by Django 3.0.8 on 2020-08-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0020_auto_20200820_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='video_id',
            field=models.CharField(default='XdhdBlPnpCw', max_length=20),
        ),
    ]