# Check the url is reachable or not

import requests
import bs4

status=requests.get("https://www.google.com")
print(status)