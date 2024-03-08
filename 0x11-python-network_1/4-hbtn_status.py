#!/usr/bin/python3
"""Write a Python script that
fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    import requests
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")
