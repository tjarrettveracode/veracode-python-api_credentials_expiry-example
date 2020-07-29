import sys
import requests
import datetime as dt
from dateutil.parser import parse
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC

from helpers import api

def creds_expire_days_warning():
    creds = api.VeracodeAPI().get_creds()
    exp = datetime.datetime.strptime(creds['expiration_ts'], "%Y-%m-%dT%H:%M:%S.%f%z")
    delta = exp - datetime.datetime.now().astimezone() #we get a datetime with timezone...
    if (delta.days < 7):
        print('These API credentials expire ', creds['expiration_ts'])

def main():

    # CHECK FOR CREDENTIALS EXPIRATION
    creds_expire_days_warning()

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