# -*- coding: utf-8 -*-
'''
具有容错性的id遍历爬虫
'''
import itertools
from download_page import download

def iteration():
    max_errors = 5 # 允许的最大错误数量
    num_errors = 0 # 记录当前错误数
    for page in itertools.count(1):
        url = 'http://www.bilibili.com/video/bangumi-two-{}.html'.format(page)
        html = download(url)
        if html is None:
            # 遇到下载出错
            num_errors += 1
            if num_errors == max_errors:
                # 错误已达到允许的最大错误数量
                break
            # 设置了最大错误数量，遇到id遍历完的情况也可以停止下来
        else:
            # 成功
            # ...
            num_errors = 0

if __name__ == '__main__':
    iteration()
'''
Downloading: http://www.bilibili.com/video/bangumi-two-1.html
Downloading: http://www.bilibili.com/video/bangumi-two-2.html
Downloading: http://www.bilibili.com/video/bangumi-two-3.html
Downloading: http://www.bilibili.com/video/bangumi-two-4.html
Downloading: http://www.bilibili.com/video/bangumi-two-5.html
Downloading: http://www.bilibili.com/video/bangumi-two-6.html
Downloading: http://www.bilibili.com/video/bangumi-two-7.html
Downloading: http://www.bilibili.com/video/bangumi-two-8.html
Downloading: http://www.bilibili.com/video/bangumi-two-9.html
Downloading: http://www.bilibili.com/video/bangumi-two-10.html
Downloading: http://www.bilibili.com/video/bangumi-two-11.html
Downloading: http://www.bilibili.com/video/bangumi-two-12.html
Downloading: http://www.bilibili.com/video/bangumi-two-13.html
Downloading: http://www.bilibili.com/video/bangumi-two-14.html
Downloading: http://www.bilibili.com/video/bangumi-two-15.html
Downloading: http://www.bilibili.com/video/bangumi-two-16.html
Downloading: http://www.bilibili.com/video/bangumi-two-17.html
Downloading: http://www.bilibili.com/video/bangumi-two-18.html
Downloading: http://www.bilibili.com/video/bangumi-two-19.html
Downloading: http://www.bilibili.com/video/bangumi-two-20.html
Downloading: http://www.bilibili.com/video/bangumi-two-21.html
Downloading: http://www.bilibili.com/video/bangumi-two-22.html
Downloading: http://www.bilibili.com/video/bangumi-two-23.html
Downloading: http://www.bilibili.com/video/bangumi-two-24.html
Downloading: http://www.bilibili.com/video/bangumi-two-25.html
Downloading: http://www.bilibili.com/video/bangumi-two-26.html
Downloading: http://www.bilibili.com/video/bangumi-two-27.html
Downloading: http://www.bilibili.com/video/bangumi-two-28.html
Downloading: http://www.bilibili.com/video/bangumi-two-29.html
Downloading: http://www.bilibili.com/video/bangumi-two-30.html
Downloading: http://www.bilibili.com/video/bangumi-two-31.html
Downloading: http://www.bilibili.com/video/bangumi-two-32.html
Downloading: http://www.bilibili.com/video/bangumi-two-33.html
Downloading: http://www.bilibili.com/video/bangumi-two-34.html
Downloading: http://www.bilibili.com/video/bangumi-two-35.html
Downloading: http://www.bilibili.com/video/bangumi-two-36.html
Downloading: http://www.bilibili.com/video/bangumi-two-37.html
...
'''
