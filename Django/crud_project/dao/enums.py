from django.db import models

class Nationality(models.TextChoices):
    PORTUGUESE = 'br', "Brazilian"
    ENGLISH = 'en', "American"
    SPANISH = 'ar', "Argentinian"