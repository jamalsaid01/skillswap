from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    # what type of skill
    SKILL_TYPE = (
        ('teach', 'I can teach'),
        ('learn', 'I want to learn'),
    )

    skill_type = models.CharField(max_length=10, choices=SKILL_TYPE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
