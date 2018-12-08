import datetime
import random

from flask import Blueprint, render_template

from apps.ext import cache

main = Blueprint('main', __name__)


# 缓存装饰器尽量写在路由下面面
# timeout单位是秒 默认永不过期
# redis  雪崩 产生的原因是同一时刻大量的数据同时过期
@main.route('/')
@cache.cached(timeout=20 + random.randint(10, 60))
def index_main():
    return render_template('index_main.html', now=datetime.datetime.now())


"""
caahed 不支持视图函数带参数
menoize 支持带参数
"""


# # 设置缓存key的名称
# def make_name():
#     return '123456'
#
#
# @main.route('/<int:id>/')
# @cache.memoize(timeout=20, make_name=make_name)
# def detail(id):
#     return render_template('index_main.html', id=id, now=datetime.datetime.now())

@main.route('/temp/')
def temp():
    return render_template('temp_cache.html', id=id, now=datetime.datetime.now())
