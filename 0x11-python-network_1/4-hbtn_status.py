#!/usr/bin/python3
"""
Script that takes in a URL, show request and send request
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    c = response.text
    print('Body response:')
    print('\t- type: {}'.format(type(c))
    print('\t- content: {}'.format(c))
