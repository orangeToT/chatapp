from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from allauth.account.forms import SignupForm
from .models import CustomUser, Message
from django import forms

# Allauthを使うため削除
# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ["username","email","password1","password2","img"]

class MySignUpForm(SignupForm):
    img = forms.ImageField()

    def save(self, request):
        user = super().save(request)
        user.img = self.cleaned_data['img']
        user.save()
        return user

class SignInForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ["username","password"]

class FriendSearchForm(forms.Form):
    search_keyword = forms.CharField(max_length=50, required=True,widget=forms.TextInput(attrs={'placeholder': 'ユーザー名を入力'}))

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