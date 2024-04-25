#!/bin/bash
# takes in a URL, sends a request to that URL
# displays the size of the body of the response
if [ $# -eq 0 ]; then
    exit 1
fi
url="$1"
response=$(curl -s -w "%{size_download}" "$url")
if [ $? -ne 0 ]; then
    exit 1
fi

echo "Size of the response body: $response bytes"

