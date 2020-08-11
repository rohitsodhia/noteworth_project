from django.db import models


class Provider(models.Model):
    name_given = models.CharField(max_length=20)
    name_family = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    clinic = models.CharField(max_length=40)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
