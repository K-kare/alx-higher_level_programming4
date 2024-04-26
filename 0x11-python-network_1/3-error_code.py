#!/usr/bin/python3
#
import urllib
import sys
try:
    with urllib.request.urlopen('sys.argv[1]') as response:
        body = response.read().decode('utf-8')
except urllib.error.HTTPError as e:
    print(e.code)
