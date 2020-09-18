#! /usr/bin/python
# -*- encoding: utf-8 -*-

'''
filename: test.py
author: 简单教程(www.twle.cn)
copyright: Copyright © 2015-2065 www.twle.cn. All rights reserved.
'''
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html; charset=utf-8')])
    return ['hello eudora']