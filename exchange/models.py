from django.db import models
from django.contrib.auth.models import User
from skills.models import Skill

class ExchangeRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')

    skill_offered = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='offered_skill')
    skill_requested = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='requested_skill')

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.receiver}"

# Create your models here.
