from django.conf import settings

from django.db import models
from django.utils import timezone


# Create your models here.
class GameTracking(models.Model):
    GAME_TYPE_CHOICES = [
        ("math_facts", "Math Facts Practice"),
        ("anagram_hunt", "Anagram Hunt"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game_type = models.CharField(max_length=20, choices=GAME_TYPE_CHOICES)
    # Store settings
    game_settings = models.JSONField()
    score = models.IntegerField(null=True, blank=True)
    # add number of tries
    tries = models.IntegerField(default=0)
    # when the user starts the game
    start_time = models.DateTimeField(auto_now_add=True)
    # when the user ends the game
    end_time = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.game_type}"
