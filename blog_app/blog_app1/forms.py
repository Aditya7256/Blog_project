from django import forms
from.models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'desc']
        labels = {'title':'Title', 'desc':'Description'}
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'desc':forms.Textarea(attrs={'class': 'form-control'}),
            
        }