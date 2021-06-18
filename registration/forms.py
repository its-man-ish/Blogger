from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from blogapp.models import UserProfile

from django import forms
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    

    class Meta:
        model = User
        fields = ('email','username','first_name','last_name','password1','password2')


class UserUpdateForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    

    class Meta:
        model = User
        fields = ('email','username','first_name','last_name')


class ProfileCreateForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('bio','profile_pic','website','facebook','twitter','linkedin','github','instagram')
        widgets ={

            
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            'website':forms.TextInput(attrs={'class':'form-control'}),
            'facebook':forms.TextInput(attrs={'class':'form-control'}),
            'twitter':forms.TextInput(attrs={'class':'form-control'}),
            'github':forms.TextInput(attrs={'class':'form-control'}),
            'linkedin':forms.TextInput(attrs={'class':'form-control'}),
            'instagram':forms.TextInput(attrs={'class':'form-control'}),



    }
