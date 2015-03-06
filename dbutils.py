# -*- coding: utf-8 -*-
import sqlite3
import config

class DBUtils(object):
    connection = None

    def __init__(self):
        pass

    def dump_sql(self, app):
        self.connect()
        with app.open_resource('schema.sql') as f:
            self.connection.cursor().executescript(f.read())
        self.connection.commit()
        self.close()

    def connect(self):
        self.connection = sqlite3.connect(config['DATABASE'])

    def close(self):
        self.connection.close()

db = DBUtils()




