from django import forms
from .models import Post

class Format(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'author': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'type': 'hidden', 'value': '', 'id': 'FormID_author'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }