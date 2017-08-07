#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 上述配置文件简单明了。但是，如果要部署到服务器时，
# 通常需要修改数据库的host等信息，直接修改config_default.py不是一个好办法，更好的方法是
# 编写一个config_override.py，用来覆盖某些默认设置：


'''
Override configurations.
'''

configs = {
    'db': {
        'host': '127.0.0.1'
    }
}