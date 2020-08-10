from django.db import models


class Provider(models.Model):
    name_given = models.CharField()
    name_family = models.CharField()
    title = models.CharField()
    clinic = models.CharField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
