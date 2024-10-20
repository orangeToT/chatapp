from django.shortcuts import redirect, render
from .models import CustomUser
from .forms import SignUpForm


def index(request):
    return render(request, "myapp/index.html")

def signup_view(request):
    if request.method == 'POST':
        # フォーム送信データを受け取る
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("myapp/index.html")

    else:
        form = SignUpForm()
    return render(request, "myapp/signup.html",{'form': form})

def login_view(request):
    return render(request, "myapp/login.html")

def friends(request):
    return render(request, "myapp/friends.html")

def talk_room(request):
    return render(request, "myapp/talk_room.html")

def setting(request):
    return render(request, "myapp/setting.html")


def signup_form(request):
    if request.method == 'POST':
        # フォーム送信データを受け取る
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("myapp/index.html")

    else:
        form = SignUpForm()

    return render(request, 'myapp/index.html', {'form': form})
