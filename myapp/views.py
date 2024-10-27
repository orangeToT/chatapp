import operator
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage

from .forms import * 
from .models import CustomUser, Message


def index(request):
    return render(request, "myapp/index.html")

# Allauthを使うため削除
#
# def signup_view(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("myapp:index")
#     else:
#         form = SignUpForm()
#     return render(request, "myapp/signup.html",{'form': form})

@login_required
def friends(request):
    user = request.user

    if request.GET.get("search_keyword"):
        form = request.GET.get('search_keyword')
        friends = CustomUser.objects.filter(
            ~Q(id=request.user.id) & Q(username__contains = form)
        ).all()
    else:
        friends = CustomUser.objects.exclude(id=request.user.id)

    form = FriendSearchForm()

    info = []
    top_message = []
    top_nomessage = []
    for friend in friends:
        latest_message = Message.objects.filter(Q(send_id=user.id,receive_id=friend.id)|Q(send_id=friend.id,receive_id=user.id)).order_by("time").last()
        if latest_message:
            top_message.append([friend.id, friend.username, friend.img, latest_message.content, latest_message.time])
        else:
            top_nomessage.append([friend.id, friend.username, friend.img, None, None])
    top_message = sorted(top_message, key=operator.itemgetter(4), reverse=True)
    info.extend(top_message)
    info.extend(top_nomessage)      

    context = {
        "info": info,
        "form": form,
    }
    return render(request, "myapp/friends.html", context)

@login_required
def talk_room(request, friend):
    send = request.user
    receive = get_object_or_404(CustomUser,id = friend)
    talk = Message.objects.filter(
        Q(send_id=send.id, receive_id=friend) | Q(send_id=friend, receive_id=send.id)
    ).order_by("time")

    form = MessageForm()
    context = {
                "form": form,
                "receive" : receive,
                "talk": talk
            }
    if request.method == 'POST':
        new_talk = Message(send=send, receive=receive)
        form = MessageForm(request.POST, instance=new_talk)

        if form.is_valid():
            form.save()
            return redirect("myapp:talk_room", friend)
        
    return render(request, "myapp/talk_room.html",context)

@login_required
def setting(request):
    return render(request, "myapp/setting.html")

@login_required
def username_change(request):
    user = request.user
    form = UsernameChangeForm
    if request.method == "POST":
        username_valid = request.POST["username"]
        form = UsernameChangeForm(request.POST, instance=user)
        try: 
            CustomUser.objects.get(username=username_valid)
            return render(request, "myapp/change_username.html",{"form":form,"error":"そのユーザ名は既に存在しています。"})
        except:
            if form.is_valid:
                form.save()
                return redirect("myapp:change_username_done")
            else:
                return render(request, "myapp/change_username.html",{"form":form,"error":"無効なユーザ名です。"})
    return render(request, "myapp/change_username.html",{"form":form})

@login_required
def username_change_done(request):
    return render(request, "myapp/change_username_done.html")

@login_required
def email_change(request):
    user = request.user
    form = EmailChangeForm
    if request.method == "POST":
        form = EmailChangeForm(request.POST, instance=user)
        if form.is_valid:
            form.save()
            return redirect("myapp:change_email_done")
    return render(request, "myapp/change_email.html",{"form":form})

@login_required
def email_change_done(request):
    return render(request, "myapp/change_email_done.html")

@login_required
def icon_change(request):
    user = request.user
    form = IconChangeForm
    if request.method == "POST":
        form = IconChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid:
            form.save()
            return redirect("myapp:change_icon_done")
    return render(request, "myapp/change_icon.html",{"form":form})

@login_required
def icon_change_done(request):
    return render(request, "myapp/change_icon_done.html")

class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    template_name = "myapp/change_password.html"
    success_url = "myapp:password_change_done"

@login_required
def password_change_done(request):
    return render(request, "myapp/change_password_done.html")

class MyLogoutView(LoginRequiredMixin, LogoutView):
    pass

# class EmailLogin(FormView):
#     template_name = ""
#     form_class = SignInEmailForm
#     success_url = "myapp:emailloginredirect"

# class EmailLoginRedirect(TemplateView,EmailMessage):
#     template_name = "myapp:login_email_redirect.html"

    
#     def __init__(self, *args, **kwargs):
#         super().send()
        