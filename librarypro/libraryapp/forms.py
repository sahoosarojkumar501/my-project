from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from .models import Details_of_book,Login_page


'''class UserLoginForm(forms.Form):
    class Meta:
        model=User
        fields=['email','password']'''
        
class Login_pages(forms.Form):
    class Meta:
        model=User
        fields=['email','password']
