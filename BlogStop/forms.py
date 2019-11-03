from django import forms
from .models import Comment

class Comment_form(forms.Form):
    name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    email = forms.EmailField(
        max_length=60,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Email"}
        ),
    )
    comment_text = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )


class Contact_form(forms.Form):
    name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    email = forms.EmailField(
        max_length=60,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "email"}
        ),
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a message!"}
        )
    )