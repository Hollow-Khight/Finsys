# 💰 Finsys

Um aplicativo simples desenvolvido em **Python** com o **Flask**, que exibe diferentes páginas HTML e demonstra rotas básicas, renderização de templates e passagem de dados entre backend e frontend.

---

## 📂 Estrutura do Projeto

```
Finsys/
│
├── Finsys/
│   ├── __pycache__/
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   ├── templates/
│   │   ├── contato.html
│   │   ├── home.html
│   │   ├── index.html
│   │   └── usuario.html
│   ├── AppFinsys.py
│   ├── AppImport.py
│   └── pyvenv.cfg
│
└── .gitignore
```

---

## 🚀 Executando o Projeto

### 1️⃣ Ative o ambiente virtual (caso tenha sido criado)

No Windows (PowerShell):
```bash
.\Scriptsctivate
```

No Linux/Mac:
```bash
source Scripts/activate
```

### 2️⃣ Instale as dependências

```bash
pip install flask
```

### 3️⃣ Execute o aplicativo

```bash
python AppFinsys.py
```

O servidor será iniciado na porta **8000**:
```
http://127.0.0.1:8000/
```

---

## 🌐 Rotas Disponíveis

| Rota | Função | Template Renderizado |
|------|---------|----------------------|
| `/` | Página inicial | `home.html` |
| `/index` | Página de índice | `index.html` |
| `/usuario` | Exibe dados do usuário | `usuario.html` |
| `/contato` | Página de contato | `contato.html` |

---

## 🧠 Lógica Principal

No arquivo `AppFinsys.py`, o aplicativo Flask é criado com:
```python
AppFinsys = Flask(__name__, template_folder='templates')
```

E as páginas são renderizadas com `render_template()`.

Exemplo da rota `/usuario`:
```python
@AppFinsys.route("/usuario")
def dados_usuario():
    dados_usu = {"nome": "Jeshua", "profissao": "Desenvolvedor", "aplicativo": "Finsys"}
    return render_template("usuario.html", dados=dados_usu)
```

Essa rota envia um dicionário `dados_usu` para o template `usuario.html`.

---

## ✨ Função Extra

O projeto também possui uma função simples de saudação:
```python
def saudacao(nome):
    return f'Olá, {nome}!'
```

---

## 🧾 Licença

Este projeto foi desenvolvido para fins educacionais e aprendizado do framework **Flask**.

---

## 👨‍💻 Autor

**Jeshua Daniel**  
Desenvolvedor do projeto **Finsys** 🧩
