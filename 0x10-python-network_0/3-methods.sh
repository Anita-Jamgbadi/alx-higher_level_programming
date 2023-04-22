#!/bin/bash
#Takes a URL and displays all HTTP methods it accepts
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
