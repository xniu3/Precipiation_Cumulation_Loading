import json
import sys
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib


def get_precip_by_year(year:int) -> list:
    try:
        ResultBytes = urllib.request.urlopen(
            "https://weather.visualcrossing.com/" +
            "VisualCrossingWebServices/rest/services/timeline/" +
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
        print('Error code: ', e.code, ErrorInfo)
        sys.exit()

    # return jsonData