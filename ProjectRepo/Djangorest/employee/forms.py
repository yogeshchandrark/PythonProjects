from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

        lable = { 'password':'Password'}

    def clean_email(self):
        if self.cleaned_data['email']:
            return self.cleaned_data['email']
        else:
            raise ValidationError("Not the correct mail format")

    def save(self):
        password = self.cleaned_data.pop('password')
        usersave = super().save()
        usersave.set_password(password)
        usersave.save()
        return usersave
