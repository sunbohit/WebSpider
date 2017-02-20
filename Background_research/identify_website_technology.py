# -*- coding: utf-8 -*-
'''
识别网站所用的技术
'''
import builtwith
tech = builtwith.parse('http://www.bilibili.com')
print tech
