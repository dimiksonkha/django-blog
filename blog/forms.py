from django import forms
from django.core import validators
from django.contrib.auth.models import User
from accounts.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio', 'profile_pic')



def check_for_s(value):
    if value[0] != 's':
        raise forms.ValidationError("name Needs to Start with S")



# This class will be workable in the next version
class PostForm(forms.ModelForm):
    title = forms.CharField(validators=[check_for_s])
    content = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_cleaned_data = super().clean()
        title = all_cleaned_data['title']
        content = all_cleaned_data['content']

        if title == content:
            raise forms.ValidationError("title and content should not be same")
