import requests
r = requests.get('https://alx-intranet.hbtn.io/status')
print(type(r.text))
print(r.text)
