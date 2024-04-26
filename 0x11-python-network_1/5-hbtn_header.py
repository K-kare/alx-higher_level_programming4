#!/usr/bin/python3
import requests
import sys
res = requests.get(sys.argv[1])
head = res.headers.get('X-Request-Id')
print(head)
