# -*- coding: utf-8 -*-
from flask import Flask
import config
from dbutils import db

app = Flask(__name__)

def configure_app(app):
    # 载入配置
    app.config.from_object(config)

    # 导入sql
    #db.dump_sql(app)

    @app.before_request
    def before_request():
        db.connect()

    @app.teardown_request
    def teardown_request(exception):
        db.close()

configure_app(app)