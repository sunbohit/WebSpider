# 爬取北京大学现代汉语语料库的数据
import urllib.parse

search = '肾脏'
value_1 = {"download_serarch_result":search}
searchstring_1 = urllib.parse.urlencode(value_1)
value_2 = {"q":search}
searchstring_2 = urllib.parse.urlencode(value_2)
print(search)
#print(searchstring)    
link = "http://ccl.pku.edu.cn:8080/ccl_corpus/search?"+searchstring_1+"&UserMaxHits=50000&dir=xiandai&"+searchstring_2+"&LastQuery=&num=50&index=FullIndex&outputFormat=TEXT&encoding=UTF-8&orderStyle=score&maxLeftLength=3000&maxRightLength=3000&scopestr="   
targetDir = "./CLLdownload/"

import requests
import shutil

r = requests.get(link, stream=True)
if r.status_code == 200:
	with open(targetDir+search+".txt", 'wb') as f:
		r.raw.decode_content = True
		shutil.copyfileobj(r.raw, f)
else:
	print(search," Error!")
	with open(targetDir+"Error.txt", 'a') as f:
		f.write(search+'\n')
