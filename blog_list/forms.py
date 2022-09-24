from django import forms
from .models import Contact
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    user = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'user forms'}), label='user')

    comment = forms.CharField(widget=forms.Textarea
                              (attrs={'class': 'comment forms'}), label='comment')

    class Meta:
        model = Contact
        fields = ("user", "comment")
