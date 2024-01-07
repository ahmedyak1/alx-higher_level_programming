#!/usr/bin/python3
"""
Script that takes in a URL, show request and send request
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        v = html.get('X-Request-Id')
        print(v)
