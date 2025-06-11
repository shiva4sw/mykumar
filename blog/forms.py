# blog/forms.py

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

        widgets = {
            'title':forms.TextInput(attrs={
                'placeholder':'Title',
                'class':'input-box',
                'required':''
                })
        }