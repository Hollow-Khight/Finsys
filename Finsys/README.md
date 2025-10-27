# 🧾 Projeto Finsys - Sistema de Gestão Financeira Pessoal (MVP)

Este projeto foi desenvolvido utilizando **Flask**, um microframework Python, como um **Mínimo Produto Viável (MVP)** para um sistema de organização e gestão financeira pessoal.  
O foco é a **usabilidade** e **segurança básica na entrada de dados**.

---

## 🚀 Funcionalidades e Implementações

O projeto implementa **validação de usuários** e inclui telas de **cadastro**, **login** e **perfil**.

### 🖥️ Backend & Segurança
- ✅ Cadastro de novos usuários  
- ✅ **Armazenamento de dados no arquivo JSON** (`users.json`)  
- ✅ **Implementação de filtros Jinja2** para formatação de CPF e Telefone na visualização de perfil (ex: `707.333.444-55`)  
- ✅ Login com verificação de e-mail e senha  
- ✅ Bloqueio de acesso a páginas sem login  
- ✅ Armazenamento seguro da sessão do usuário com `SECRET_KEY`  
- ✅ Logout do usuário  

### 🎨 Frontend & Usabilidade
- ✅ **Design customizado** com paleta de cores laranja/branco (inspirado no Banco Inter)  
- ✅ **Validação de e-mail duplicado** no momento do cadastro  
- ✅ **Validação de senha robusta** (mínimo de 6 caracteres, 1 maiúscula, 1 número, 1 caractere especial)  
- ✅ **Máscaras automáticas** via JavaScript para CPF e Telefone (melhorando a entrada de dados)  
- ✅ Exibição dos dados do usuário logado na página de perfil  
- ✅ Página de contato com dados do desenvolvedor e foto de perfil  

---

## 🧠 Estrutura do Projeto

```
📁 Finsys/
│
├── static/
│   ├── CSS/
│   │   └── style.css               # Estilos globais e de layout
│   ├── Imagens/
│   │   ├── logo_finsys.png         # Logotipo do aplicativo
│   │   └── perfil_desenvolvedor.jpg # Foto de perfil do dev (página Contato)
│   └── JavaScript/
│       └── script.js               # Lógica de máscaras (CPF, Telefone) e validação
│
├── templates/                      # Páginas HTML do sistema
│   ├── apresentacao.html
│   ├── base.html
│   ├── cadastro.html
│   ├── contato.html
│   ├── index.html
│   ├── login.html
│   └── usuario.html
│
├── AppFinsys.py                    # Código principal do Flask (arquivo que você executa)
├── users.json                      # Arquivo de armazenamento dos usuários
└── README.md                       # Este arquivo
```

---

## ⚙️ Tecnologias Utilizadas

- **Python 3**
- **Flask**
- **Jinja2** (templating)
- **HTML5**
- **JSON** (banco de dados simulado)
- **CSS3** (estilização customizada)
- **JavaScript** (máscaras e validações)

---

## 🧩 Como Executar o Projeto

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/Hollow-Khight/Finsys.git
cd Finsys
```

### 2️⃣ Crie e ative um ambiente virtual
```bash
python -m venv venv
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 3️⃣ Instale as dependências
```bash
pip install flask
```

### 4️⃣ Execute o servidor Flask
```bash
python AppFinsys.py
```

### 5️⃣ Acesse no navegador
```
http://127.0.0.1:5000
```

---

💡 **Dica:**  
Você pode editar as páginas HTML e os arquivos CSS/JS livremente na pasta `static/` e `templates/` para personalizar o design do sistema conforme desejar.
