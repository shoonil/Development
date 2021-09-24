from django.db.models import fields
from rest_framework import serializers
from .models import Membership

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model=Membership
        fields=['id',
                'FullName',
                'CurrentAddress', 
                'Email',
                'MobileNumber', 
                'Birthdate', 
                'PermanentAddress', 
                'P_state', 
                'P_district',
                'p_local_level',
                'p_ward',
                'p_tole',
                'i_agree']
    # FullName=serializers.CharField(max_length=100, default='')
    # CurrentAddress=serializers.CharField(max_length=100, default='')
    # Email=serializers.EmailField(blank=True, default='')
    # MobileNumber=serializers.BigIntegerField
    # Birthdate=serializers.DateField(blank=True, null=True)
    # PermanentAddress=serializers.CharField(max_length=100, default='')
    # P_state=serializers.CharField(max_length=100, default='')
    # P_district=serializers.CharField(max_length=100, default='')
    # p_local_level=serializers.CharField(max_length=100, default='')
    # p_ward=serializers.BigIntegerField
    # p_tole=serializers.CharField(max_length=100, default='')
    # i_agree=serializers.BooleanField( null=True)

    # def create(self, validated_data):
    #     return Membership.objects.create(validated_data)
        
    # def update(self,instance, validated_data):
    #     instance.FullName= validated_data.get('FullName', instance.FullName)
    #     instance.CurrentAddress= validated_data.get('CurrentAddress', instance.CurrentAddress)
    #     instance.Email= validated_data.get('Email', instance.Email)
    #     instance.MobileNumber= validated_data.get('MobileNumber', instance.MobileNumber)
    #     instance.Birthdate= validated_data.get('Birthdate', instance.Birthdate)
    #     instance.PermanentAddress= validated_data.get('PermanentAddress', instance.PermanentAddress)
    #     instance.P_state= validated_data.get('P_state', instance.P_state)
    #     instance.P_district= validated_data.get('P_district', instance.P_district)
    #     instance.p_local_level= validated_data.get('p_local_level', instance.p_local_level)
    #     instance.p_ward= validated_data.get('p_ward', instance.p_ward)
    #     instance.p_tole= validated_data.get('p_tole', instance.p_tole)
    #     instance.i_agree= validated_data.get('i_agree', instance.i_agree)
        
    #     return Membership.objects.create(validated_data)
        
    # def create(self, validated_data):
    #     return Membership.objects.create(validated_data)