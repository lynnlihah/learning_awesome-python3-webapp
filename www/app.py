'''web app 骨架'''
'''由于Web框架使用了基于asyncio的aiohttp，这是基于协程的异步模型。在协程中，不能调用普通的同步
IO操作，因为所有用户都是由一个线程服务的，协程的执行速度必须非常快，才能处理大量用户的请求。而
耗时的IO操作不能在协程中以同步的方式调用，否则，等待一个IO操作时，系统无法响应任何其他用户。'''

# 由于我们的Web App建立在asyncio的基础上，因此用aiohttp写一个基本的app.py：
import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')
    # return web.Response(body=b'<h1>Awesome</h1>') 不填写 content_type 会自动变成下载页面

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return  srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
