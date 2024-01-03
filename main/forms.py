from django import forms
from .models import ContactMessageModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessageModel
        fields = ['full_name', 'email', 'phone_number', 'subject', 'message']

    full_name = forms.CharField(
        label='Full Name',
        widget=forms.TextInput(attrs={'placeholder': 'Your Full Name'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'Your email address'})
    )
    phone_number = forms.CharField(
        label='Phone (optional)',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Your phone number'})
    )
    subject = forms.ChoiceField(
        label='Subject',
        choices=[
            ('', 'Select a subject'),
            ('subject1', 'Influencer'),
            ('subject2', 'Working Together'),
            ('subject3', 'Question & Help'),
        ],
        widget=forms.Select(attrs={'style': 'background: black'})
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'placeholder': 'Write your message here ...'})
    )
