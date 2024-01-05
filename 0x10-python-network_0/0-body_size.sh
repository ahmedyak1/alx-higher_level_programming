#!/bin/bash
# scrippt that takes in a URL, sends a request to that URL, and shows size of body of the respon

curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
