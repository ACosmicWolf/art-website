from xml.etree.ElementTree import Comment
from django.forms import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','comment']
