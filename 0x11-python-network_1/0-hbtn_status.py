#!/usr/bin/python3
#Python script that fetches an url
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
