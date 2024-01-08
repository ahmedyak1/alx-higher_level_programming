#!/usr/bin/python3
"""
Script that takes in a URL, show request and send request
"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    payload = {"q": q}
    res = requests.post(url, data=payload)
    try:
        jo = res.json()
        if not jo:
            print("No result")
        else:
            m_id = jo.get("id")
            m_name = jo.get("name")
            print("[{}] {}".format(m_id, m_name))
    except ValueError as invalid_json:
        print("Not a valid JSON")
