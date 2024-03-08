#!/usr/bin/python3
""" Write a Python script that fetches
https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        if 'X-Request-Id' in response.headers:
            request_id = response.headers['X-Request-Id']
            print(f"{request_id}")
