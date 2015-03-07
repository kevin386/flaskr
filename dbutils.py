# -*- coding: utf-8 -*-
import sqlite3
import config

class DBUtils(object):
    conn = None
    curr = None

    def __init__(self):
        pass

    @property
    def cursor(self):
        return self.conn.cursor()

    def connect(self):
        self.conn = sqlite3.connect(config.DATABASE)

    def close(self):
        self.conn.close()

    def execute(self, *args):
        self.curr = self.conn.execute(*args)

    def commit(self):
        self.conn.commit()

    def fetchall(self):
        return self.curr.fetchall()

    def dump_sql(self, app):
        self.connect()
        with app.open_resource('schema.sql') as f:
            self.cursor.executescript(f.read())
        self.commit()
        self.close()

    def dump_test_data(self):
        self.connect()
        sql_scripts = "INSERT INTO entries(title, text) VALUES('python', 'python is usefull');"
        sql_scripts += "INSERT INTO entries(title, text) VALUES('linux', 'linux is powerfull');"
        sql_scripts += "INSERT INTO entries(title, text) VALUES('java', 'java is heavy');"
        sql_scripts += "INSERT INTO entries(title, text) VALUES('lua', 'lua is good');"
        sql_scripts += "INSERT INTO entries(title, text) VALUES('ruby', 'ruby is hard');"
        self.cursor.executescript(sql_scripts)
        self.commit()
        self.close()

db = DBUtils()




