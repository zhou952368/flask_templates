import datetime

from apps.ext import db


class User_cache(db.Model):
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, index=True, nullable=False)
    # 查询字段
    # lazy= 'dynamic' 选项只能用户一对多或者多对多的关系
    # uselist  默认为True (一对多)  False 为一对一
    image = db.relationship('Image', back_populates='user', uselist=False)


class Image(db.Model):
    ing_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    path = db.Column(db.String(255), unique=True, default='')
    # 1 表示用户头像 2  商品信息图片
    type = db.Column(db.SmallInteger, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    # 外键字段
    uid = db.Column(db.Integer, db.ForeignKey(User_cache.uid), unique=True)
    # 查询字段
    user = db.relationship('User', back_populates='image', uselist=False)
