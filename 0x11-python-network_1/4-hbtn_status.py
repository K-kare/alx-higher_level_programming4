#!/usr/bin/python3
#Python script that fetches a url
import requests
res = requests.get("https://alx-intranet.hbtn.io/status")
print("Body response:")
print("\t- type:", type(res))
print("\t- content:", res)
