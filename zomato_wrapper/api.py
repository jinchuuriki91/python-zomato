from bs4 import BeautifulSoup
from zomato_wrapper.base import get_page
from zomato_wrapper.constants import BASE_URL


def get_countries(tag=None):
    soup = BeautifulSoup(get_page(BASE_URL), features="html.parser")
    countries_resultset = soup.find("footer", {"id": "footer"}).findChildren("a", {"class": "pl5"})
    resp = [{
        "name": x.get_text(strip=True),
        "url": x.get("href", None),
        "tag": x.get("href", "").split('/')[-1]
    } for x in countries_resultset]
    if tag:
        fil = list(filter(lambda x: x["tag"] == tag, resp))
        return fil[0] if fil else None
    return resp


def get_cities(country_tag):
    country = get_countries(country_tag)
    if not country:
        return None
    soup = BeautifulSoup(get_page(country["url"]), features="html.parser")
    city_resultset = soup.findChildren("a", {"style": "flex-grow: 1;"})
    resp = [{
        "name": x.get_text(strip=True),
        "url": x.get("href", None)
    } for x in city_resultset]
    return resp
