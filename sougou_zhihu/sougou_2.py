"http://zhihu.sogou.com/zhihu?query="
from pyquery import PyQuery as pq


def get_answer(question):
	doc = pq("http://zhihu.sogou.com/zhihu?query="+question)
	for i in range(10):
		lwp = doc('#zhihu_summary_answer_'+str(i))
		condidate = lwp.text().strip('泻药').strip('谢邀')
		if condidate[-3:] != '...':
			return condidate

question = '聪明人有哪些表现？'
print(get_answer(question))

