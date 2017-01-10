import requests
 
r = requests.get('http://llhelper.duapp.com/llnewcarddata') 
print(type(r)) #<class 'requests.models.Response'>
print(r.status_code) # 200
print(r.encoding) # utf-8
#print(r.text) #
print(r.cookies) #<RequestsCookieJar[<Cookie BAEID=7F9C5A399877EE7CA1ACE39CDFFA2DC8 for llhelper.duapp.com/>]>


r = requests.post("http://httpbin.org/post")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")

