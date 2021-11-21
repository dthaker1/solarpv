from django import forms
from django.core.exceptions import ValidationError

from backend.models import User


class RegisterForm(forms.ModelForm):
    firstname = forms.CharField(label="first name", max_length=100)
    lastname = forms.CharField(label="last name", max_length=100)
    middlename = forms.CharField(label="middle name", max_length=100)
    username = forms.CharField(label="username", max_length=100)
    email = forms.EmailField(label="email")
    password = forms.CharField(label="password", max_length=100)

    def clean_usertype(self):
        usertype = self.cleaned_data["usertype"]
        if usertype not in ["client", "staff"]:
            raise ValidationError("Usertype can either be staff or client")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return usertype

    class Meta:
        model = User
        fields = [
            "firstname",
            "lastname",
            "middlename",
            "username",
            "email",
            "password",
            "usertype",
        ]
