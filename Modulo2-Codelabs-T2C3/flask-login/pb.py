from flask import Blueprint

pb = Blueprint ('pb', __name__)

@pb.route("/")
def home():
    return "<h1> Hello, Flask! </h1>"

@pb.route("/login/<nome>")
def login(nome=None):
    return "<center><h1>Fala aí, "+ nome +"! <br/>Faça seu login!</h1></center>"