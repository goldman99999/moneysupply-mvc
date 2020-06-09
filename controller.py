# coding:utf-8
import jinja2
from model.models import *


def get_tpl(file_path, **kwargs):  # 参数： 文件路径
    with open(file_path, 'r') as f:
        html = f.read()  # 获取模板内容
        tpl = jinja2.Template(html)  # 传入jinja2模板引擎 返回模板对象
        html = tpl.render(**kwargs)  # 渲染完的html内容
    return html.encode('utf-8')


def main_page():
    pic = './static/pboc_logo.jpg'
    date, m2g_date, m1g_date, m1g_m2g_date, df = data()
    return get_tpl('views/mainPage.html', pic=pic, date=date, m2g_date=m2g_date, m1g_date=m1g_date,
                   m1g_m2g_date=m1g_m2g_date, df=df)


