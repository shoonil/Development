# Generated by Django 3.2.3 on 2021-09-06 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(default='', max_length=100)),
                ('CurrentAddress', models.CharField(default='', max_length=100)),
                ('Email', models.EmailField(blank=True, default='', max_length=254)),
                ('MobileNumber', models.IntegerField()),
                ('Birthdate', models.DateField(blank=True, null=True)),
                ('PermanentAddress', models.CharField(default='', max_length=100)),
                ('P_state', models.CharField(default='', max_length=100)),
                ('P_district', models.CharField(default='', max_length=100)),
                ('p_local_level', models.CharField(default='', max_length=100)),
                ('p_ward', models.BigIntegerField()),
                ('p_tole', models.CharField(default='', max_length=100)),
                ('i_agree', models.BooleanField(null=True)),
            ],
        ),
    ]
