#!/usr/bin/python3
#Python script that fetches an url
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read().decode('utf-8')
    print("\t- Body response:")
    print("\t\t- type:", type(body))
    print("\t\t- content:", body)
    print("\t- utf8 content:", body)
