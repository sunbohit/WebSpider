import requests

r = requests.get('http://subhd.com/type/%E5%8A%A8%E7%94%BB/2')
print(r.text)
print("_________________________________________________")
print(type(r))
print(r.status_code)
print(r.encoding)
print(r.cookies)
