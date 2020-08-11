from django.urls import path

from authtokens.views import get

urlpatterns = [
    path("", get, name="get_token"),
]
