from django import forms

class PostForm(forms.Form):
    titile = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
