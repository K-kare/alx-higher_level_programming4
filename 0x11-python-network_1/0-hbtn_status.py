#!/usr/bin/python3
#Python script that fetches
if __name__ == "__main__":
    import urllib.request
    """
    Python module for fetching url
    body : variable stores the response
    """
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        body = response.read().decode('utf-8')
    print("Body response:")
    print("\t\t- type:", type(body))
    print("\t\t- content:", body)
    print("\t\t- utf8 content:", body)
