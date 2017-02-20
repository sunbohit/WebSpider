# -*- coding: utf-8 -*-
'''
页面下载
'''
import urllib2
import urlparse


def download1(url):
    # 通过url请求，下载页面
    return urllib2.urlopen(url).read()


def download2(url):
    # 加入异常处理的url页面下载
    print 'Downloading:', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
    return html


def download3(url, num_retries=2):
    # 4xx错误发生在请求存在问题时，如404页面不存在
    # 5xx错误发生在服务器端，如503服务器过载
    # 5xx错误可以尝试重新下载
    print 'Downloading:', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # 重新尝试解决 5XX HTTP 错误
                html = download3(url, num_retries-1)
    return html


def download4(url, user_agent='sunbohit', num_retries=2):
    #为防止默认用户代理被封禁，使用自定义用户代理
    print 'Downloading:', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # 重新尝试解决 5XX HTTP 错误
                html = download4(url, user_agent, num_retries-1)
    return html


def download5(url, user_agent='wswp', proxy=None, num_retries=2):
    # 支持代理功能的url下载方式（不稳定）
    print 'Downloading:', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html = opener.open(request).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # 重新尝试解决 5XX HTTP 错误
                html = download5(url, user_agent, proxy, num_retries-1)
    return html


download = download5


if __name__ == '__main__':
    print download('http://www.bilibili.com')
