
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import config
from dbutils import *

app = Flask(__name__)
app.config.from_object(config.__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
