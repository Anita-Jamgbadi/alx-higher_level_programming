#!/bin/bash
# displays the status code ONLY of the response from a URL
curl -s -o /dev/null -w "%{http_code}" "$1"
