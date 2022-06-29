from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100, required=True)
    last_name = forms.CharField(label="Last Name", max_length=100, required=True)
    email = forms.EmailField(label="Email", max_length=100, required=True)