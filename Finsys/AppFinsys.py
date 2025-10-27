from flask import Flask, render_template, request, redirect, url_for, session, g
import json, os

JSON_FILE = 'users.json'
SECRET_KEY = os.environ.get('SECRET_KEY') or 'sua_chave_secreta_e_unica'

AppFinsys = Flask(__name__, template_folder='templates')
AppFinsys.secret_key = SECRET_KEY

def format_cpf(value):
    """Formata CPF para xxx.xxx.xxx-xx."""
    if not value:
        return ""
    cpf = str(value).replace('.', '').replace('-', '')
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return str(value)

def format_phone(value):
    """Formata telefone para (xx) xxxxx-xxxx ou (xx) xxxx-xxxx."""
    if not value:
        return ""
    phone = str(value).replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
    
    if len(phone) == 11: # (XX) XXXXX-XXXX
        return f"({phone[:2]}) {phone[2:7]}-{phone[7:]}"
    elif len(phone) == 10: # (XX) XXXX-XXXX
        return f"({phone[:2]}) {phone[2:6]}-{phone[6:]}"
    return str(value)

AppFinsys.jinja_env.filters['format_cpf'] = format_cpf
AppFinsys.jinja_env.filters['format_phone'] = format_phone

def carregar_usuarios():
    if not os.path.exists(JSON_FILE):
        return []
    try:
        with open(JSON_FILE, 'r') as f:
            content = f.read()
            return json.loads(content) if content else []
    except (json.JSONDecodeError, IOError):
        return []

def salvar_usuarios(users_list):
    
    try:
        with open(JSON_FILE, 'w') as f:
            json.dump(users_list, f, indent=4)
        return True
    except IOError:
        return False


@AppFinsys.before_request
def load_logged_in_user():
    g.user = None
    if 'user_email' in session:
        users = carregar_usuarios()
        
        g.user = next((user for user in users if user['email'] == session['user_email']), None)

        if g.user is None:
            session.pop('user_email', None)
    
    
    g.endpoint = request.endpoint

@AppFinsys.route('/')
def apresentacao():
    if g.user:
        return redirect(url_for('index'))
    else:
        return render_template('apresentacao.html')

@AppFinsys.route('/index')
def index():
    if not g.user:
        return redirect(url_for('apresentacao'))
    
    return render_template('index.html')

@AppFinsys.route('/login', methods=['GET', 'POST'])
def login():
    if g.user:
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        users = carregar_usuarios()
        user_data = next((user for user in users if user['email'] == email and user['senha'] == senha), None)
        
        if user_data:
            session['user_email'] = user_data['email']
            return redirect(url_for('index')) 
        else:
            return render_template('login.html', erro_login="Email ou senha inválidos.")

    return render_template('login.html')

@AppFinsys.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if g.user:
        return redirect(url_for('index'))

    if request.method == 'POST':
        nome_completo = request.form.get('nome_completo')
        cpf = request.form.get('cpf')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        endereco = request.form.get('endereco')
        senha = request.form.get('senha')
        confirma_senha = request.form.get('confirma_senha')

        if senha != confirma_senha:
            return render_template('cadastro.html', erro_cadastro="As senhas não coincidem.")
            
        users = carregar_usuarios()
        if any(user.get('email') == email for user in users):
            return render_template('cadastro.html', erro_cadastro="Este e-mail já está cadastrado.")

        novo_usuario = {
            'nome_completo': nome_completo,
            'cpf': cpf,
            'email': email,
            'telefone': telefone,
            'endereco': endereco,
            'senha': senha,
        }

        users.append(novo_usuario)
        if salvar_usuarios(users):
            return redirect(url_for('login')) 
        else:
            return render_template('cadastro.html', erro_cadastro="Erro ao salvar o usuário.")

    return render_template('cadastro.html')

@AppFinsys.route('/perfil')
def dados_usuario():
    if not g.user:
        return redirect(url_for('apresentacao')) 

    return render_template('usuario.html', user=g.user)

@AppFinsys.route('/contato')
def contato():
    if not g.user:
        return redirect(url_for('apresentacao'))
        
    return render_template('contato.html')

@AppFinsys.route('/logout')
def logout():
    session.pop('user_email', None)
    return redirect(url_for('apresentacao'))


if __name__ == '__main__':
    if not os.path.exists(JSON_FILE):
        salvar_usuarios([])
        
    AppFinsys.run(port=8000, debug=True)