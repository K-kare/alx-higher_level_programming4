#!/bin/bash
#script that takes in a URL as an argument,and sends a get request
curl -s -X GET "$1" -H "X-School-User-Id: 98" | echo 
