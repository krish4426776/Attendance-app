from  . models import Attendance  , Room , Notification
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms


class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password' ]

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'
        exclude = ['user' , 'name' ]
        
      


class Roomform(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        widgets = {
            'datee': forms.DateInput(attrs={'type': 'date'})
        }

class NotiicationForm(ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'