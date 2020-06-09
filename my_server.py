# coding:utf-8
from wsgiref.simple_server import make_server
from controller import *


# 路由映射信息表
urls = {
    '/': main_page,
}


def application(env, start_response):
    start_response('200 ok', [('Content-Type', 'text/html')])  # 设置响应类型和状态码
    url = env['PATH_INFO']
    if url in urls:
        fuc = urls.get(url, None)
        if fuc is not None:
            return fuc()
    else:
        return '404 page'


if __name__ == '__main__':
    http_server = make_server('127.0.0.1', 8088, application)  # 创建httpserver
    http_server.serve_forever()  # 启动服务
