#!/usr/bin/python3
""" Write a Python script that takes in a URL, sends a request
to the URL and displays the body of the
response (decoded in utf-8)."""

if __name__ == "__main__":
    import urllib.request
    import sys
    from urllib import *
    from urllib.error import *

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            decoded_body = response.read().decode('utf-8')
            print(f"{decoded_body}")
    except HTTPError as e:
        print('Error code:', e.code)
