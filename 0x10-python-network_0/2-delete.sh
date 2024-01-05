#!/bin/bash
# scrippt that sends a del request to the URL passed as the first args and shows the body of the response
curl -s "$1" -X DELETE
