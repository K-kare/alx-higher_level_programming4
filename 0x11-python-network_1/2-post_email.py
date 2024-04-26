#!/usr/bin/python3
#
import sys
import urllib
email = email.encode('utf-8')
with urllib.request.urlopen(sys.argv[1], sys.argv[2]) as response:
    body = response.read().decode('utf-8')
    print(response_body)
if __name__ == "__main__":
    if len(sys.argv) != 3:
         sys.exit(1)
