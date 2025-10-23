from flask import Flask

AppFinsys = Flask (__name__)

@AppFinsys.route('/')
@AppFinsys.route('/ola')

def raiz():
    return 'Olá, Meu nome é Jeshua Daniel'

def saudacao (nome):
    return f'Olá, {nome}!'

if __name__ == "__main__" :
    AppFinsys.run(port = 8000)
