from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=40, required=True)
    email = forms.EmailField(max_length=254, required=True)
    subject = forms.CharField(max_length=20, required=True, )
    message = forms.CharField(widget=forms.Textarea, required=True)