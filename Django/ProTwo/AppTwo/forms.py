from django import forms
from django.forms import ModelForm
from AppTwo.models import UsersRecord
from django.core import validators

class MyForm(ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label = 'Enter your email again:')
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("make sure emails match")
    class Meta():
        model = UsersRecord
        fields = '__all__'
