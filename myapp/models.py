from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    img = models.ImageField(blank=True, null=True)
    first_name = None
    last_name = None

class Message(models.Model):
    send = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="send")
    receive = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="receive")
    content = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True,blank=True,null=True)