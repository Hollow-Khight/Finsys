# 🧾 Projeto Flask - Sistema de Cadastro e Login com Validação de Usuários

Este projeto foi desenvolvido utilizando **Flask**, um microframework Python para criação de aplicações web.  
O objetivo de hoje foi implementar **validação de usuários**, com **telas de cadastro, login e perfil**, utilizando um **arquivo JSON** para armazenamento dos dados.

---

## 🚀 Funcionalidades Principais

✅ Cadastro de novos usuários  
✅ Validação de e-mail duplicado  
✅ Login com verificação de e-mail e senha  
✅ Armazenamento seguro da sessão do usuário  
✅ Exibição dos dados do usuário logado  
✅ Bloqueio de acesso a páginas sem login  
✅ Logout do usuário

---

## 🧠 Estrutura do Projeto

```
📁 seu_projeto/
│
├── templates/              # Páginas HTML do sistema
│   ├── apresentacao.html
│   ├──base.html
│   ├── cadastro.html
│   ├── contato.html
│   ├── index.html
│   ├── login.html
│   └── usuario.html
│
├── AppFinsys.py                  # Código principal do Flask (arquivo que você executa)
│
└── README.md               # Este arquivo
```

---

## ⚙️ Tecnologias Utilizadas

- **Python 3**
- **Flask**
- **HTML5**
- **JSON**
- (Opcional) **CSS / Bootstrap** para estilização

---

## 🧩 Como Executar o Projeto

1. **Clone o repositório**
   ```bash
   git clone https://github.com/Hollow-Khight/Finsys.git
   cd Finsys
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv Finsys

3. **Ative o ambiente**
   ```bash
   source venv/bin/activate     # Linux/Mac
   Finsys\Scripts\activate      # Windows
   ```

4. **Instale as dependências**
   ```bash
   pip install flask
   ```

5. **Execute o servidor Flask**
   ```bash
   python AppFinsys.py
   ```

6. **Acesse no navegador:**
   ```
   http://127.0.0.1:8000
   ```

---

## 🔒 Segurança e Sessões

- O sistema utiliza uma **chave secreta (SECRET_KEY)** para proteger as sessões.  
- As rotas protegidas exigem que o usuário esteja logado. 
- O arquivo `users.json` é criado automaticamente quando é cadastrada uma pessoa.
- O login é validado com base no arquivo `users.json`, que guarda os dados cadastrados.

---

## 👤 Autor

**Jeshua Daniel**  
Projeto criado para estudo e prática com Flask.  
Dia 26/10/2025: Implementação de cadastro, login, validação e controle de sessão de usuários.

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais e acadêmicos.
