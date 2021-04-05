import requests
req=requests.get('https://www.google.com')
if '200' in str(req):
    print(f'site is available {req}')