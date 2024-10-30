from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    img = models.ImageField(upload_to='',blank=True, null=True)
    first_name = None
    last_name = None

class Message(models.Model):
    send = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="sent_message")
    receive = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="received_message")
    content = models.CharField(max_length=500,null=True)
    time = models.DateTimeField(auto_now_add=True,blank=True,null=True)