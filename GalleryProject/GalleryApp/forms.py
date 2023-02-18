from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from .models import ImageModel



class LoginForm(AuthenticationForm):
    
    username = forms.CharField( label='Enter Username' ,widget =forms.TextInput(attrs={'class':'form-control'}) )
    password = forms.CharField(label = 'Enter Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username' , 'password']


class RegisterForm(UserCreationForm):

 

    password1 = forms.CharField(label='Enter Password' , widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(label='Confirm Password' , widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name' , 'last_name' , 'username' , 'email' ]

        labels = {
            'first_name':'Enter First Name ',
            'lst_name' : 'Enter Last Name',
            'username' : 'Enter Username',
            'email' : 'Enter Email-ID'
        }
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'})
        }

        
class AddImageForm(forms.ModelForm):

    class Meta:
        model = ImageModel
        fields = ['title' , 'desc' , 'cat' , 'image']

        labels = {
            'title':'Enter Image Title',
            'desc' : 'Enter Image Description',
            'cat' : 'Select Image Category',
            'image' : 'Upload Image'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-control'}),
            'desc' : forms.Textarea(attrs={'class' : 'form-control'}),
            'cat' : forms.Select(attrs={'class' : 'form-control'}),
            'image' : forms.FileInput(attrs={'class' : 'form-control'})
            
        }