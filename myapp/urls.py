from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

app_name = "myapp"
urlpatterns = [
    path('', views.index, name='index'),
    path('friends', views.friends, name='friends'),
    path('talk_room/<int:friend>', views.talk_room, name='talk_room'),
    path('setting', views.setting, name='setting'),
    path('changeusername', views.username_change, name='change_username'),
    path('changeusernamedone', views.username_change_done, name='change_username_done'),
    path('changeemail', views.email_change, name='change_email'),
    path('changeemail', views.email_change_done, name='change_email_done'),
    path('changeicon', views.icon_change, name='change_icon'),
    path('changeicondone', views.icon_change_done, name='change_icon_done'),
    path('changepassword', views.PasswordChange.as_view(), name='change_password'),
    path('changepassworddone', views.password_change_done, name='password_change_done'),
    path('logout', views.MyLogoutView.as_view(), name='logout'),
    # path('signup', views.signup_view, name='signup_view'),
    # path('login', LoginView.as_view(template_name='myapp/login.html',form_class=SignInForm), name='login_view'),
]
