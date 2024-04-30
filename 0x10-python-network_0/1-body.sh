#!/bin/bash
#that takes in a URL, sends a GET request to the URL.
curl -s -L  -o get.txt -w "%{http_code}" "$1" 
