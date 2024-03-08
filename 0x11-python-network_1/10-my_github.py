#!/usr/bin/python3
""" sends a request to the URL and
displays the body of the response."""

if __name__ == "__main__":
    from requests.auth import HTTPBasicAuth
    import sys
    import requests
    import json
    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get('https://api.github.com/user', auth=basic)
    res = response.json()
    print(res.get('id'))
