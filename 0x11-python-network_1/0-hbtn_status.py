#!/usr/bin/python3
#Python script that fetches an url
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read()
    print("\t- Body response:")
    print("\t\t- type:", type(body))
    print("\t\t- content:", body)
