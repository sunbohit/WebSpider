# -*- coding: utf-8 -*-

import itertools
from download_page import download


def iteration():
    for page in itertools.count(1):
    #下载bilibili新番页面
        url = 'http://www.bilibili.com/video/bangumi-two-{}.html'.format(page)
        html = download(url)
        if html is None:
            # 下载页面时出现了错误
            # 很可能是到达了最后一个页面
            break
        else:
            # 下载成功
            pass

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
