# -*- coding: utf-8 -*-

import re
from download_page import download


def crawl_sitemap(url):
    # 下载网站地图文件
    sitemap = download(url)
    # 抽取链接
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # 逐一下载链接
    for link in links:
        html = download(link)
        # 随后处理html


if __name__ == '__main__':
    crawl_sitemap('http://blog.csdn.net/sitemap-index-1.xml') # CSDN博客的网站地图

