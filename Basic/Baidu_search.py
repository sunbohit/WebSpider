# 百度搜索结果页面获取
import urllib
import urllib.request
 
data={}
data['word']='凉宫春日'
 
url_values=urllib.parse.urlencode(data) # url字符转码
url="http://www.baidu.com/s?"
full_url=url+url_values
 
data=urllib.request.urlopen(full_url).read() #读取页面
data=data.decode('UTF-8') # utf-8解码
print(data)
