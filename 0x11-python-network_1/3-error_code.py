#!/usr/bin/python3
"""
Script that takes in a URL, show request and send request
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            rt = response.read().decode("utf-8")
            print(rt)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
