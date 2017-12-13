"""
app.py編寫Web APP骨架
"""


import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    ''' 
    響應函數 注意：Response中必須加content_type = 'text/html'，這樣才能在瀏覽器中顯示
    '''
    return web.Response(body=b'<h1>Awesome!</h1>', content_type = 'text/html')

@asyncio.coroutine
def init(loop):
    # Web App服務器初始化
    # 制作響應合集
    app = web.Application(loop=loop)

    # 把響應函數添加到響應函數合集
    app.router.add_route('GET', '/', index)
    # app.router.add_route(method = 'GET', path = '/', handler = index)

    # 創建服務器（鏈接網址、端口，綁定handler）
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    
    logging.info('server started at http://127.0.0.1:9000...')
    
    return srv

# 創建事件
loop = asyncio.get_event_loop()

# 運行
loop.run_until_complete(init(loop))

# 服務器不關閉
loop.run_forever()
