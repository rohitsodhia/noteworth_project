from django.shortcuts import render
from requests.exceptions import RetryError

from noteworth_project.utils import requests_retry_session

from authtokens.models import AuthToken

# Create your views here.
def get(request):
    context = {
        "request_failed": False,
    }
    try:
        r = requests_retry_session().get("http://127.0.0.1:5000/auth")
    except RetryError:
        context["request_failed"] = True
    else:
        new_token = AuthToken(token=r.headers["Super-Secure-Token"])
        new_token.save()
    return render(request, "authtokens.html", context)
