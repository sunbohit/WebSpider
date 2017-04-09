"http://zhihu.sogou.com/zhihu?query="
from pyquery import PyQuery as pq
question = '聪明人有哪些表现？'
doc = pq("http://zhihu.sogou.com/zhihu?query="+question)

#print(doc.html())
#print(type(doc))
lwp = doc('#zhihu_summary_answer_0')
#print(type(lwp))
zhihu_url = lwp.attr.href
print(zhihu_url)

doc = pq(zhihu_url)
lwp = doc('.RichText CopyrightRichText-richText')
print(lwp.text())

