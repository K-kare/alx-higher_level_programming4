#!/bin/bash
# takes in a URL, sends a request to that URL.
response=$(curl -s -o /dev/null -w "%{size_download}" "$1")
