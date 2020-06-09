from flask import Flask, request, render_template, jsonify, session
from Currency import *


app = Flask(__name__)
app.config["SECRET_KEY"] = "idgafkltsic"


@app.route('/')
def show_index():
    return render_template('index.html')