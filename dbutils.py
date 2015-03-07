# -*- coding: utf-8 -*-
import sqlite3
import config

class DBUtils(object):
    db = None
    curr = None

    def __init__(self):
        pass

    def dump_sql(self, app):
        self.connect()
        with app.open_resource('schema.sql') as f:
            self.db.cursor().executescript(f.read())
        self.db.commit()
        self.close()

    def connect(self):
        self.db = sqlite3.connect(config.DATABASE)

    def close(self):
        self.db.close()

    def execute(self, expression):
        self.curr = self.db.execute(expression)

    def commit(self):
        self.db.commit()

    def fetchall(self):
        return self.curr.fetchall()

db = DBUtils()




