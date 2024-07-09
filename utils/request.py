import requests
import os

def make_login_api_request(endpoint, payload):
    # Endpoint de registro da api de login
    url = "http://localhost:3000/"

    if os.path.exists('/.dockerenv'):
        url = "http://financial-control-login-mvp-1:3000/"

    # Request
    return requests.post(url + endpoint, payload)

def make_financial_control_api_request(method, payload):
    # Endpoint de registro da api de login
    url = "http://localhost:5002/bill_items"

    if os.path.exists('/.dockerenv'):
        url = "http://financial-control-mvp-2:5002/bill_items"

    # Requests
    if method == "POST":
        return requests.post(url, files=payload)
    elif method == "PUT":
        return requests.put(url, files=payload)
    elif method == "DELETE":
        return requests.delete(url, files=payload)
    else:
        query = "?user_id=" + payload
        return requests.get(url + query)