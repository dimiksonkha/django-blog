from django import forms
from django.core import validators
from django.contrib.auth.models import User
from accounts.models import UserProfileInfo

#UserForm for Registraiton
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

#UserProfileInfoForm for Registraiton
class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio', 'profile_pic')
