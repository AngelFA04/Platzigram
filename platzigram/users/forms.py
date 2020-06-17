""" User forms. """

#Django
from django import forms

#

class SignupForm(forms.Form):
    
    username = forms.CharField(min_length=4, max_length=50)
    password = forms.CharField(min_length=4, max_length=70, widget=forms.PasswordInput() )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(min_length=6, max_length=90, widget=forms.EmailInput())

class ProfileForm(forms.Form):
    """Profile form."""

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField( max_length=20, required=False)
    picture = forms.ImageField()
    
    
