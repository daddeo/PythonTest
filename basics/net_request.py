# install the MySQL connector with PyCharm
# 1. open command prompt
# 2. run "pip install requests"
#
# dependencies: certifi, urllib3, idna, chardet
# current as of now is v2.23.0

import requests

r = requests.get("http://www.google.com")
print(r.elapsed)
print(r.encoding)
print(r.headers)
print(r.raw)
print(r.status_code)
print(r.url)
