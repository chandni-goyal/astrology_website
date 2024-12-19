from django.db import models

class UserPreference(models.Model):
    name = models.CharField(max_length=50)
    zodiac_sign = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
