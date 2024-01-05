#!/bin/bash
# scrippt that takes in a URL, sends a POST request to the passed URL, and shows the body of the resp
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
