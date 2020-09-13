from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm



class SignupForm(UserCreationForm):
    username=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email=forms.CharField(label='',widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password1=forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2=forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Re-enter Password'}))
   
    class Meta:
        model=User
        fields=('username','email')


    def clean_email(self,*args,**kwargs):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("email alreday taken")
        else:
            return self.cleaned_data.get('email')

            

class LoginForm(forms.Form):
    username=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password=forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

    def clean_username(self,*args,**kwargs):
        if not User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError("Username does not exist")
        else:
            return self.cleaned_data.get('username')
