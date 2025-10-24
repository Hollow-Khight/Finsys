from flask import Flask, render_template

AppFinsys = Flask (__name__, template_folder='templates')

@AppFinsys.route("/")
def home():
    return render_template ('home.html')

@AppFinsys.route("/contato")
def contato():
    return render_template ('contato.html')

def saudacao (nome):
    return f'Olá, {nome}!'

if __name__ == "__main__" :
    AppFinsys.run(port = 8000)