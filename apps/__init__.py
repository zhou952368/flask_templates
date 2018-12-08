from flask import Flask
from apps.email.views import email
from apps.ext import init_ext
from apps.main.views import main
from apps.req.views import req
from apps.upload.views import upload


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config['SECRET_KEY'] = 'sadasdasd1213231123'
    init_ext(app)
    register_bp(app)
    return app


def register_bp(app):
    app.register_blueprint(req, url_prefix='/req')
    app.register_blueprint(email, url_prefix='/email')
    app.register_blueprint(main)
    app.register_blueprint(upload, url_prefix='/upload')
