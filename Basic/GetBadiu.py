import urllib.request

url = "http://www.baidu.com"
a = urllib.request.urlopen(url)
data = a.read()
data = data.decode('UTF-8')
#print(data)
#print(type(a))
'''
<class 'http.client.HTTPResponse'>
'''
#print(a.geturl())
'''
http://www.baidu.com
'''
#print(a.info())
'''
Date: Thu, 29 Dec 2016 11:32:53 GMT
Content-Type: text/html; charset=utf-8
Transfer-Encoding: chunked
Connection: Close
Vary: Accept-Encoding
Set-Cookie: BAIDUID=9F1183E77CA32FE557BCBBD57457FAF1:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
Set-Cookie: BIDUPSID=9F1183E77CA32FE557BCBBD57457FAF1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
Set-Cookie: PSTM=1483011173; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
Set-Cookie: BDSVRTM=0; path=/
Set-Cookie: BD_HOME=0; path=/
Set-Cookie: H_PS_PSSID=1451_21107_17001_21553_20927; path=/; domain=.baidu.com
P3P: CP=" OTI DSP COR IVA OUR IND COM "
Cache-Control: private
Cxy_all: baidu+bae901aec379a4013d26d3498af78d08
Expires: Thu, 29 Dec 2016 11:32:48 GMT
X-Powered-By: HPHP
Server: BWS/1.1
X-UA-Compatible: IE=Edge,chrome=1
BDPAGETYPE: 1
BDQID: 0xf4e51ca800088f9e
BDUSERID: 0


'''
print(a.getcode())
'''
200
'''
