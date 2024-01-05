#!/bin/bash
# scrippt that takes in a URL as an arg, sends a GET request to the URL, and shows the body of the response
curl -s "$1" -H "X-School-User-Id: 98"
