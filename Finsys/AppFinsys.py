from flask import Flask

AppFinsys = Flask (__name__)

@AppFinsys.route('/')
def raiz():
    return 'Olá, turma!'

AppFinsys.run()
