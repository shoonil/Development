# Generated by Django 3.2.3 on 2021-09-06 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlfnepal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='MobileNumber',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='membership',
            name='p_ward',
            field=models.CharField(default='', max_length=100),
        ),
    ]
