from django import forms
from django.contrib.auth.models import User
from .models import *


class userreg(forms.Form):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']

# class meta:it is usually the inner class which is basically used to provid emeta data to the model fom or the model class it is used to change the brhaviour of your existing form

class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    conf=forms.CharField(max_length=20,widget=forms.PasswordInput)
    class Meta:
            model=User
            fields=['username','first_name','last_name','email','password']


class userlogin(forms.Form):
     username=forms.CharField(max_length=20)
     password=forms.CharField(max_length=50)

    # __all__ constructor
    # __all__ is a field that indicates all fields all fields in model should be include in forms
    # __all__ return a list of model fields

class regform(forms.ModelForm):
     password=forms.CharField(widget=forms.PasswordInput)
     class Meta:
          model = regmodel
          fields='__all__' 

class logform(forms.Form):
     email=forms.EmailField()
     password=forms.CharField(max_length=50, widget=forms.PasswordInput)
