#!/usr/bin/python3
# Python script that takes in a URL, 
#sends a request to the URL and displays the value of the X-Request-Id
import urllib
import sys
if len(sys.argv) < 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)
url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print("X-Request-Id:", x_request_id)
        else:
            print("X-Request-Id header not found in the response.")

