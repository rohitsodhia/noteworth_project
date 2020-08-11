from django.http import HttpResponse
from django.shortcuts import render

from authtokens.models import AuthToken

# Create your views here.
def landing(request):
    context = {"last_token": None}
    try:
        auth_token = AuthToken.objects.filter().order_by("-createdAt")[0]
    except IndexError:
        pass
    else:
        context["last_token"] = auth_token.createdAt
    return render(request, "landing.html", context)

