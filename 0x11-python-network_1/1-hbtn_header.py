#!/usr/bin/python3
# Python script that takes in a URL, 
#sends a request to the URL and displays the value of the X-Request-Id
import urllib
import sys
if len(sys.argv) < 2:
    sys.exit(1)
with urllib.request.urlopen(sys.argv[1]) as response:

