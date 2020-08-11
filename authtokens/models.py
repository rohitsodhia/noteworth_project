from django.db import models


class AuthToken(models.Model):
    token = models.CharField(max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True)

    @classmethod
    def latest(cls):
        try:
            auth_token = cls.objects.order_by("-createdAt")[0]
        except IndexError:
            auth_token = None
        return auth_token
