from flask import Flask, render_template

AppFinsys = Flask (__name__, template_folder='templates')

@AppFinsys.route("/")
def home():
    return render_template ('home.html')

@AppFinsys.route("/index")
def indice():
    return render_template ('index.html')

@AppFinsys.route("/usuario")
def dados_usuario():
    dados_usu = {"nome": "Jeshua", "profissao": "Desenvolvedor", "aplicativo":"Finsys"}
    return render_template ("usuario.html", dados = dados_usu)

@AppFinsys.route("/contato")
def contato():
    return render_template ('contato.html')

def saudacao (nome):
    return f'Olá, {nome}!'

if __name__ == "__main__" :
    AppFinsys.run(port = 8000)