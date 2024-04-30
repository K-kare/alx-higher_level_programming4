#!/bin/bash
# takes in a URL, sends a request to that URL
# displays the size of the body of the response
response=$(curl -s  -w "%{size_download}" "$1")
echo $response
