from flask import Blueprint, request

req = Blueprint('req', __name__)


@req.route('/hello/', methods=['get', 'post'])
def hello():
    if request.method == 'GET':
        request.args.get('name')
        # 获取请求中所有的值.既能获取get请求的数据也能获取post的数据
        request.values.get('name ')
        # 相当于post请求
        # request.form.get()
        # 获取文件对象
        # request.files
        # 获取cookie信息
        # request.cookies
        # 获取解析好的json字符串
        # request.json
        # 获取原生的json数据
        # request.get_data()
    elif request.method == 'POST':
        pass
