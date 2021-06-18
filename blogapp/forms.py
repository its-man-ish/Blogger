from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'username','type':'hidden'}),
        }


class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('name','body')
        widgets ={

        
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),

    }
