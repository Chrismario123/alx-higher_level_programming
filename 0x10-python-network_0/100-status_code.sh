#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code
curl -s -o null --write-out "%{http_code}" "$1"
