from django import forms
from django.db.models import fields
from django.forms.fields import DateField
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class ComplaintForm(forms.ModelForm):
    
    class Meta:
        model=complaint
        fields=('Email','first_name','last_name','address','location','area','detail',)


class ComplaintReply(forms.ModelForm):
    class Meta:
        model=complaint
        fields=('reply',)





class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields='__all__'


class NewsForm(forms.ModelForm):
    class Meta:
        model=News
        fields='__all__'



class FIRForm(forms.ModelForm):
    class Meta:
        model=FIR
        fields=('station',)
