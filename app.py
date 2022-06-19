from flask import Flask
from flask import render_template

server = Flask(__name__)


@server.route('/plotly_dashboard') 
def render_dashboard():
    return flask.redirect('/pathname')
