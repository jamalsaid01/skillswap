from django.db import models
from django.contrib.auth.models import User
from exchange.models import ExchangeRequest

class Message(models.Model):
    exchange = models.ForeignKey(ExchangeRequest, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} - {self.text[:20]}"

# Create your models here.
