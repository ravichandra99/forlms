# Generated by Django 3.0.8 on 2020-08-23 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0026_auto_20200823_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='reviews',
            field=models.FloatField(verbose_name='rating'),
        ),
    ]
