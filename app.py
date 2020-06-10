from flask import Flask, request, render_template, jsonify, session
from Convert import *


app = Flask(__name__)
app.config["SECRET_KEY"] = "idgafkltsic"


@app.route('/')
def show_index():
    """ SHow home route """
    return render_template('index.html')

@app.route("/convert", methods=["POST"])
def get_conversion():
    """ revice calues ot convert and update for conversion """
    ch_from = request.args["form"]
    ch_to = request.args["to"]
    amount = request.args["amount"]
