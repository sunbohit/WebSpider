from pyspider.libs.base_handler import *

PAGE_START = 1
PAGE_END = 23
DIR_PATH = './ass/'

outputfile=DIR_PATH+'ar_url.txt'
fileopen = open(outputfile,'w')
print('open')

class Handler(BaseHandler):
    crawl_config = {
    }
    def __init__(self):
        self.base_url = 'http://subhd.com/type/%E5%8A%A8%E7%94%BB/'
        self.page_num = PAGE_START
        self.total_num = PAGE_END

    @every(minutes=24 * 60)
    def on_start(self):
        while self.page_num <= self.total_num:
            url = self.base_url + str(self.page_num)
            self.crawl(url, callback=self.index_page)
            self.page_num += 1

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            if 'do0' in each.attr.href:
                print(each.attr.href)
                self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            if 'ar0' in each.attr.href:
                print(each.attr.href)
                fileopen.write(each.attr.href)
                self.crawl(each.attr.href, callback=self.download_page)
                
    @config(priority=3)
    def download_page(self, response):
        for each in response.doc('.btn-sm').items():
            if '点击下载字幕文件' in each.text():
                print(each.text())
            #if 'ar0' in each.attr.href:
            #    print(each.attr.href)
                #self.crawl(each.attr.href, callback=self.download_page, fetch_type='js')
                
fileopen.close()
