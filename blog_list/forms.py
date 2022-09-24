from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    user = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'user forms'}), label='user')

    comment = forms.CharField(widget=forms.Textarea
                              (attrs={'class': 'comment forms'}), label='comment')

    class Meta:
        model = Comment
        fields = ("user", "comment")
