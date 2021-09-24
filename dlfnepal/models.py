from django.db import models


# Create your models here.


class Membership(models.Model):
    FullName=models.CharField(max_length=100, default='')
    CurrentAddress=models.CharField(max_length=100, default='')
    Email=models.EmailField(blank=True, default='')
    MobileNumber=models.CharField(max_length=100, default='')
    Birthdate=models.DateField(blank=True, null=True)
    PermanentAddress=models.CharField(max_length=100, default='')
    P_state=models.CharField(max_length=100, default='')
    P_district=models.CharField(max_length=100, default='')
    p_local_level=models.CharField(max_length=100, default='')
    p_ward=models.CharField(max_length=100, default='')
    p_tole=models.CharField(max_length=100, default='')
    i_agree=models.BooleanField( null=True)