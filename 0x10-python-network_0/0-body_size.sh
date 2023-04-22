#!/bin/bash
#This script takes a URL and displays the size of
#the body of the response

RESPONSE=$(curl -s "$1")
LENGTH=$(echo -n "$RESPONSE" | wc -c)
echo $LENGTH
