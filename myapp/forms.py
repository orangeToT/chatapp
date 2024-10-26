from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Message
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username","email","password1","password2","img"]

class SignInForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ["username","password"]

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("content",)
        labels = {
            "content":""
        }
        widgets = {"talk": forms.TextInput(attrs={"autocomplete": "off"})}

class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("username",)
        labels = {
            "username":"New username"
        }

class EmailChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email",)
        labels = {
            "email":"New email"
        }

class IconChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("img",)
        labels = {
            "img":"New icon"
        }