from json.decoder import JSONDecodeError

from django.shortcuts import render
from requests.exceptions import RetryError

from noteworth_project.utils import requests_retry_session, generate_auth_header

from authtokens.models import AuthToken
from providers.models import Provider

# Create your views here.
def get(request):
    context = {
        "no_auth_token": False,
        "request_failed": False,
        "invalid_json": False,
        "providers": [],
    }

    auth_token = AuthToken.latest()
    if not auth_token:
        context["no_auth_token"] = True

    try:
        r = requests_retry_session().get(
            "http://127.0.0.1:5000/providers",
            headers=generate_auth_header(auth_token.token, "providers"),
        )
    except RetryError:
        context["request_failed"] = True

    try:
        r.json()
    except JSONDecodeError:
        context["invalid_json"] = True
    else:
        for provider_dict in r.json()["providers"]:
            context["providers"].append(Provider(**provider_dict))
        Provider.objects.bulk_create(context["providers"])

    return render(request, "providers.html", context)
