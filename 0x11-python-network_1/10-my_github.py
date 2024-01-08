#!/usr/bin/python3
"""
Script that takes in a URL, show request and send request
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    usern = sys.argv[1]
    passwordd = sys.argv[2]
    resp = requests.get(url, auth=HTTPBasicAuth(usern, passwordd))
    jo = resp.json()
    print(jo.get("id"))
