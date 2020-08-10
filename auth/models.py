from django.db import models


class AuthToken(models.Model):
    token = models.CharField()
    createdAt = models.DateTimeField(auto_now_add=True)
