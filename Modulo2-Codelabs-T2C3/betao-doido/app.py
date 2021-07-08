from flask import Flask, render_template

app = Flask('__name__')

@app.route('/<status>')
def index(status=None):
    nome = "Betão"
    sobrenome = "Einstein"
    idade = 46

    if status == "doido":
        doido = True
    else:
        doido = False

    img_serio = "https://upload.wikimedia.org/wikipedia/commons/5/50/Albert_Einstein_%28Nobel%29.png"
    img_doido = "https://www.hypeness.com.br/1/2017/08/EinsteinL3.jpg"

    return render_template('index.html', nome=nome, sobrenome=sobrenome, idade=idade, img_doido=img_doido, img_serio=img_serio, doido=doido)

if (__name__ == '__main__'):
    app.run(debug=True)