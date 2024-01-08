#!/usr/bin/python3
"""
Script that takes in a URL, show request and send request
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    b = res.text
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(b)
