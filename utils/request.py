import requests
import os

def make_login_api_base_request(endpoint, payload):
    # Endpoint de registro da api de login
    url = "http://localhost:3000/"

    if os.path.exists('/.dockerenv'):
        url = "http://financial-control-login-mvp-1:3000/"

    # Request
    return requests.post(url + endpoint, payload)