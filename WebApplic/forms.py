__author__ = 'yura'

from WebApplic.models import Comment
from django.forms import ModelForm

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']