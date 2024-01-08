#!/usr/bin/python3
"""
Script that takes in a URL, show request and send request
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {
        "email": email
    }
    r = requests.post(url, data=payload)
    print(r.text)
