#!/usr/bin/python3
""" Write a Python script that takes in a
URL and an email, sends a POST"""

if __name__ == "__main__":
    import urllib.request
    import sys
    from urllib import *

    jsondata = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(jsondata).encode('utf-8')
    with urllib.request.urlopen(sys.argv[1], data=data) as response:
        decoded_body = response.read().decode('utf-8')
        print(f"{decoded_body}")
