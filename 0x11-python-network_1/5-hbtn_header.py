#!/usr/bin/python3
# Python script that takes in a URL
# displays the value of the variable 
import requests
import sys
res = requests.get(sys.argv[1])
head = res.headers.get('X-Request-Id')
print(head)
