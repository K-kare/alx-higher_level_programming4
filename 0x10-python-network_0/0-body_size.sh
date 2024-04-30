#!/bin/bash
# takes in a URL, sends a request to that URL
# displays the size of the body of the response
if [ -z "$1" ]; then
    exit 1
fi
response=$(curl -s  -w "%{size_download}" "$1")
echo $response

