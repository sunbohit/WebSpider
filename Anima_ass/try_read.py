# 获取入口索引页面
import urllib
import urllib.request

url="http://subhd.com/type/%E5%8A%A8%E7%94%BB"
full_url=url
data=urllib.request.urlopen(full_url).read() #读取页面
data=data.decode('UTF-8') # utf-8解码
print(data)

url = "http://subhd.com/do0/26359260"
full_url=url
data=urllib.request.urlopen(full_url).read() #读取页面
data=data.decode('UTF-8') # utf-8解码
print(data)

url = "http://subhd.com/ar0/357007"
full_url=url
data=urllib.request.urlopen(full_url).read() #读取页面
data=data.decode('UTF-8') # utf-8解码
print(data)
