from flask import Flask, render_template
from pb import pb
from pb2 import pb2

app = Flask(__name__)

app.register_blueprint(pb)
app.register_blueprint(pb2)

if __name__ == '__main__':
    app.run(debug=True)