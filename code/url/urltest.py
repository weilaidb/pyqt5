#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
import sys
import urllib
from urllib import request


listweb = ['https://www.baidu.com',
           'https://redis.io/',
           'https://github.com/weilaidb',
           'https://www.liaoxuefeng.com',
           'https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000',
            'http://www.douban.com/',
           ]

for webaddr in listweb:
    print("==============web addr :%s\n\n" % webaddr)
    try:
        #如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，
        # 我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页：
        req = request.Request(webaddr)
        req.add_header('User-Agent',
                       'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
        with request.urlopen(req) as f:
            data = f.read()
            print('Status:', f.status, f.reason)
            for k, v in f.getheaders():
                print('%s: %s' % (k, v))
            print('Data:', data.decode('utf-8'))
    except Exception:
        print("unable to parse web:%s" % webaddr)


