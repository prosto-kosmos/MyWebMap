from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS

class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'



class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password', 'first_name', 'last_name', 'email')
        help_texts={'username': ''}
        labels={
            'first_name': 'Имя (не обязательно):',
            'last_name' : 'Фамилия (не обязательно):', 
            'email':'Адрес электронной почты (не обязательно):',
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user