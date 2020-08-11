import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from hashlib import sha256


def requests_retry_session(
    retries=2, backoff_factor=0.3, status_forcelist=(408, 500, 502, 504), session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


def generate_auth_header(token, path):
    return {"X-Request-Checksum": sha256(f"{token}/{path}".encode("utf-8")).hexdigest()}
