# Generated by Django 3.0.8 on 2020-08-23 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0024_auto_20200821_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='offer_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='original_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='video_id',
            field=models.CharField(default='XdhdBlPnpCw', max_length=20, verbose_name='Introduction Video ID'),
        ),
    ]
