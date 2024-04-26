#!/usr/bin/python3
# Python script that takes in a URL
# displays the value of the variable 
import requests
import sys
res = requests.get(sys.argv[1])
head = res.headers.get('X-Request-Id')
print(head)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py sys.argv[1]")
        sys.exit(1)
