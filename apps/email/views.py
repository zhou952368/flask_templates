from flask_mail import Message
from flask import Blueprint
from apps.ext import mail

email = Blueprint('email', __name__)


@email.route('/index/')
def index():
    msg = Message(subject='Hello World',
                  sender='15571383682@163.com',
                  body='来自大哥的问候',
                  recipients=['15571383682@163.com'])
    mail.send(msg)
    return '发送成功'
