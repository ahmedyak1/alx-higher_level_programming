#!/usr/bin/python3
"""
Script that takes in a URL, show request and send request
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    p = {
        "email": email
    }
    query_string = urllib.parse.urlencode(p)
    data = query_string.encode("ascii")
    reqe = urllib.request.Request(url, data)
    with urllib.request.urlopen(reqe) as response:
    
        rt = response.read().decode("utf-8")
        print(rt)
