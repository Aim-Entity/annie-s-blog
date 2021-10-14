from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'name forms'}), label='Name')

    email = forms.CharField(widget=forms.EmailInput
                            (attrs={'class': 'email forms'}), label='Email')

    subject = forms.CharField(widget=forms.TextInput
                              (attrs={'class': 'subject forms'}), label='Subject')

    message = forms.CharField(widget=forms.Textarea
                              (attrs={'class': 'message forms'}), label='Message')

    class Meta:
        model = Contact
        fields = ("name", "email", "subject", "message")
