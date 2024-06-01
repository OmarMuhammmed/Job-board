from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SingupForm(UserCreationForm):
     class Meta:
      model = User
      fields =['username','email','password1','password2']
    
class EditUser(forms.ModelForm):
     class Meta:
      model = User
      fields =['username', 'first_name','last_name','email']
    
class EditProfile(forms.ModelForm):
     class Meta:
      model = Profile
      fields =['phone_number','city','image']
    
