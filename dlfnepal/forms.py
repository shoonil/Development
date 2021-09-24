from django import forms

class MembershipForm(forms.Form):
    FullName=forms.CharField(label='')
    CurrentAddress=forms.CharField()
    Email=forms.EmailField()
    MobileNumber=forms.CharField()
    Birthdate=forms.DateField()
    PermanentAddress=forms.CharField()
    P_state=forms.CharField()
    P_district=forms.CharField()
    p_local_level=forms.CharField()
    p_ward=forms.CharField()
    p_tole=forms.CharField()
    i_agree=forms.BooleanField()