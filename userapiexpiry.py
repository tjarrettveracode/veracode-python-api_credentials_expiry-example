import sys
import requests
import datetime as dt
from dateutil.parser import parse
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC


#api_base = "https://api.veracode.com/appsec/v1"
api_base = "https://api.veracode.com/api/authn/v2"
headers = {"User-Agent": "Python HMAC Example"}


if __name__ == "__main__":

    try:
        response = requests.get(api_base + "/users", auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
    except requests.RequestException as e:
        print("Whoops!")
        print(e)
        sys.exit(1)

    if response.ok:
        data = response.json()
        for user in data["_embedded"]["users"]:
            try:
                response2 = requests.get(api_base + "/users/" + user["user_id"], auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
            except requests.RequestException as e2:
                print("Whoops!")
                print(e2)
                sys.exit(1)
            if response2.ok:
                data2 = response2.json()
                if "api_credentials" in data2:
                    date_time_str = parse(data2["api_credentials"]["expiration_ts"])
                    date = date_time_str.date()
                    time = date_time_str.time()
                    print("User: "+ user["user_name"] + " API Credentials expiration date is "+ str(date) + " " + str(time))
                else:
                    print("User: "+ user["user_name"] + " has no API credentials")
            else:
                print(response2.status_code)
    else:
        print(response.status_code)
