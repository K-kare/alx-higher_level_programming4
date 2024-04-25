#!/usr/bin/python3
import request
# takes in a URL, sends a request to that URL
# displays the size of the body of the response
if [ $# -eq 0 ]; then
    exit 1
fi
url="$1"
response=$(curl -s -o /tmp/curl_response.tmp -w "%{size_download}" "$url")
