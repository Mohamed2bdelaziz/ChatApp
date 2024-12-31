from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.

class Chat(models.Model):
    name = models.CharField(null=False, max_length=60)
    users = models.ManyToManyField(User, related_name='chats')
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Ensure at least one user is associated with the chat
        if not self.users.exists():
            raise ValidationError("A chat must have at least one user.")

    def save(self, *args, **kwargs):
        # Call clean method to enforce validation
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Chat {self.name} between: {', '.join(user.username for user in self.users.all())}"

class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} in Chat {self.chat.name} @ {self.timestamp}"

