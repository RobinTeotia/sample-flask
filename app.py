from flask import Flask
from flask import render_template

server = Flask(__name__)


@server.route("/")
def hello_world():
    return render_template("dash.py")
