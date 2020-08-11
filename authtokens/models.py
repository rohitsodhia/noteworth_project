from django.db import models


class AuthToken(models.Model):
    token = models.CharField(max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True)
