# Veracode Python API Credentials Expiry using HMAC Example

A simple example to get the expiration dates of api credentials for your users.

## Setup

Clone this repository:

    git clone https://github.com/tjarrettveracode/veracode-python-api_credentials_expiry-example

Install dependencies:

    cd veracode-python-api_credentials_expiry-example
    pip install -r requirements.txt

(Optional) Save Veracode API credentials in `~/.veracode/credentials`

    [default]
    veracode_api_key_id = <YOUR_API_KEY_ID>
    veracode_api_key_secret = <YOUR_API_KEY_SECRET>
	
## Run

If you have saved credentials as above you can run:

    python userapiexpiry.py
    
Otherwise you will need to set environment variables before running `example.py`:

    export VERACODE_API_KEY_ID=<YOUR_API_KEY_ID>
    export VERACODE_API_KEY_SECRET=<YOUR_API_KEY_SECRET>
    python userapiexpiry.py
	
NOTE: To be able to use all the endpoints of the Identity REST APIs, you must have one of these account types:

    API service account with the Admin API role.
    user account with the Administrator role.
	
as described here: https://help.veracode.com/go/c_identity_intro
