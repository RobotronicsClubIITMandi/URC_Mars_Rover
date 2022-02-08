from cProfile import label
from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea({'rows': 5}))