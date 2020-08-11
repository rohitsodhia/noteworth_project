from django.http import HttpResponse
from django.shortcuts import render

from authtokens.models import AuthToken

# Create your views here.
def landing(request):
    context = {"last_token": None}
    auth_token = AuthToken.latest()
    if auth_token:
        context["last_token"] = auth_token.createdAt
    return render(request, "landing.html", context)

