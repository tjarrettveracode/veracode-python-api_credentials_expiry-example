import sys
import requests
import datetime as dt
from dateutil.parser import parse
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC

from helpers import api

def main():

    data = api.VeracodeAPI().get_users()

    for user in data:
        data2 = api.VeracodeAPI().get_user(user["user_id"])

        if "api_credentials" in data2:
            date_time_str = parse(data2["api_credentials"]["expiration_ts"])
            date = date_time_str.date()
            time = date_time_str.time()
            print("User: "+ user["user_name"] + " API Credentials expiration date is "+ str(date) + " " + str(time))
        else:
            print("User: "+ user["user_name"] + " has no API credentials")
        

if __name__ == '__main__':
    main()