import sys
import requests
import datetime
from dateutil.parser import parse

from veracode_api_py import VeracodeAPI as vapi

def creds_expire_days_warning():
    creds = vapi().get_creds()
    exp = datetime.datetime.strptime(creds['expiration_ts'], "%Y-%m-%dT%H:%M:%S.%f%z")
    delta = exp - datetime.datetime.now().astimezone() #we get a datetime with timezone...
    if (delta.days < 7):
        print('These API credentials expire {}'.format(creds['expiration_ts']))

def main():
    # CHECK FOR CREDENTIALS EXPIRATION
    creds_expire_days_warning()

    data = vapi().get_users()

    for user in data:
        data2 = vapi().get_user(user["user_id"])

        if "api_credentials" in data2:
            date_time_str = parse(data2["api_credentials"]["expiration_ts"])
            date = date_time_str.date()
            time = date_time_str.time()
            print("User {} API Credentials expiration date is {} {}".format(user["user_name"],str(date),str(time)))
        else:
            print("User {} has no API credentials".format(user["user_name"]))
        

if __name__ == '__main__':
    main()