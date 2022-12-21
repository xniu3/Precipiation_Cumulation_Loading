import json
import sys
import ssl
import urllib
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
ssl._create_default_https_context = ssl._create_unverified_context


def get_precip_by_year(year: int) -> list:
    try:
        ResultBytes = urllib.request.urlopen(
            "https://weather.visualcrossing.com/" + "VisualCrossingWebServices/rest/services/timeline/" +
            "280%20Vanderbilt%20Beach%20Rd%2C%20Naples%2C%20FL%2034108/" +
            str(year) + "-12-11/" + str(year) + "-12-15" +
            "?unitGroup=metric&key=JSU4FDB6ZE6EN59D753EPKHJG&contentType=json")
        # Parse the results as JSON
        jsonData = json.loads(ResultBytes.read().decode('utf-8'))
        precip = list()
        for _, daydict in enumerate(jsonData["days"]):
            precip.append(daydict["precip"])
        return precip
    except urllib.error.HTTPError as e:
        ErrorInfo = e.read().decode()
        print('API request failed with status code: ', e.code, ErrorInfo)
        sys.exit()

    # return jsonData


def get_precip_by_year_(date: datetime) -> list:
    delta = relativedelta(days=5)
    url = "https://weather.visualcrossing.com/" + "VisualCrossingWebServices/rest/services/timeline/" + \
            "280%20Vanderbilt%20Beach%20Rd%2C%20Naples%2C%20FL%2034108/" + \
            (date-delta).strftime('%Y-%m-%d') + "/"  + \
            date.strftime('%Y-%m-%d') + \
            "?unitGroup=metric&key=JSU4FDB6ZE6EN59D753EPKHJG&contentType=json"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("API request failed with status code: " + str(response.status_code))
    else:
        data = response.json()
    return [day["precip"] for day in data["days"]]


def get_precip_by_date(date: datetime) -> list:
    delta = relativedelta(days=5)
    url = "https://weather.visualcrossing.com/" + "VisualCrossingWebServices/rest/services/timeline/" + \
            "280%20Vanderbilt%20Beach%20Rd%2C%20Naples%2C%20FL%2034108/" + \
            (date-delta).strftime('%Y-%m-%d') + "/"  + \
            date.strftime('%Y-%m-%d') + \
            "?unitGroup=metric&key=JSU4FDB6ZE6EN59D753EPKHJG&contentType=json"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("API request failed with status code: " + str(response.status_code))
    else:
        data = response.json()
    return [day["precip"] for day in data["days"]]


def get_precip_today() -> list:
    date = datetime.now()
    delta = relativedelta(days=5)
    url = "https://weather.visualcrossing.com/" + "VisualCrossingWebServices/rest/services/timeline/" + \
            "280%20Vanderbilt%20Beach%20Rd%2C%20Naples%2C%20FL%2034108/" + \
            (date-delta).strftime('%Y-%m-%d') + "/"  + \
            date.strftime('%Y-%m-%d') + \
            "?unitGroup=metric&key=JSU4FDB6ZE6EN59D753EPKHJG&contentType=json"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("API request failed with status code: " + str(response.status_code))
    else:
        data = response.json()
    return [day["precip"] for day in data["days"]]