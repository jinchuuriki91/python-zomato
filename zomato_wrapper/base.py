# Python imports
import requests

# Project imports
from zomato_wrapper.constants import HEADERS


def get_page(url, **headers):
    _headers = {**HEADERS, **headers}
    resp = requests.get(url, headers=_headers)
    resp.raise_for_status()
    return resp.content
