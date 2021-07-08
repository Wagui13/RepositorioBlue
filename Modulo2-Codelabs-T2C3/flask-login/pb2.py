from flask import Blueprint, render_template

pb2 = Blueprint('pb2',__name__)

@pb2.route("/blue/")
def carrega():
    return render_template('blue.html')