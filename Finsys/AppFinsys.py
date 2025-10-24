from flask import Flask

AppFinsys = Flask (__name__)

@AppFinsys.route('/')
@AppFinsys.route('/index')

def indice():
    return 'Olá, Meu nome é Jeshua Daniel'

@AppFinsys.route('/rota1')
def rota1():
    resposta = "<H3> Esta é uma rota criada e separada do index </H3>"
    return resposta

def saudacao (nome):
    return f'Olá, {nome}!'

if __name__ == "__main__" :
    AppFinsys.run(port = 8000)