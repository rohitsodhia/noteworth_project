from django.urls import path

from providers.views import get

urlpatterns = [
    path("", get, name="providers"),
]
