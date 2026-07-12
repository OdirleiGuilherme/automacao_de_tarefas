# 🤖 Automação de Cadastro de Produtos com Python

Este projeto automatiza o cadastro de produtos em um sistema web utilizando **Python**, **PyAutoGUI** e **Pandas**.

A aplicação abre o Microsoft Edge, acessa o sistema, realiza o login utilizando credenciais armazenadas em um arquivo `.env`, lê uma planilha CSV com os produtos e preenche automaticamente o formulário de cadastro.

---

## 🚀 Funcionalidades

- Abertura automática do Microsoft Edge;
- Login automático utilizando variáveis de ambiente (`.env`);
- Leitura de dados do arquivo `produtos.csv`;
- Cadastro automático de produtos;
- Preenchimento automático dos campos do formulário;
- Suporte à interrupção da automação levando o mouse ao canto superior esquerdo da tela;
- Rolagem automática da página para continuidade do cadastro.

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- PyAutoGUI
- Pandas
- NumPy
- python-dotenv


---

## 📂 Estrutura do Projeto

```text
📁 automacao_de_tarefas
│── main.py
│── produtos.csv
│── .env              # Não enviar ao GitHub
│── .env.example      # Exemplo de configuração
│── .gitignore
│── requirements.txt
│── README.md
```

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/automacao_de_tarefas.git
```

Entre na pasta do projeto:

```bash
cd automacao_de_tarefas
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Caso ainda não tenha o arquivo `requirements.txt`, utilize:

```bash
pip install pyautogui pandas numpy python-dotenv keyboard
```

---

## ⚙️ Configuração

Crie um arquivo chamado `.env` na raiz do projeto.

Exemplo:

```env
EMAIL=seu_email@hotmail.com
PASSWORD=sua_senha
LINK=https://dlp.hashtagtreinamentos.com/python/intensivao/login
```

O projeto utiliza essas variáveis para realizar o login automaticamente.

---

## ▶️ Como Executar

Certifique-se de que:

- o arquivo `produtos.csv` esteja na pasta do projeto;
- o arquivo `.env` esteja configurado corretamente.

Execute:

```bash
python main.py
```

O programa irá:

1. Abrir o Microsoft Edge;
2. Acessar o sistema;
3. Realizar o login;
4. Ler os produtos do arquivo CSV;
5. Cadastrar automaticamente todos os produtos.

---

## 📄 Formato do Arquivo CSV

O arquivo `produtos.csv` deve conter as seguintes colunas:

| codigo | marca   | tipo | categoria   | preco_unitario | custo |   obs    |
|--------|---------|------|-------------|----------------|-------|----------|
|   001  | Samsung | TV   | Eletrônicos |      2500      | 1800  | estoque  |
|   002  |  Dell   |Laptop| Informática |      4500      | 3800  |  NaN     |

---

## ⌨️ Interrompendo a Automação

Durante a execução, é possível interromper a automação utilizando o recurso de segurança do PyAutoGUI movendo o cursor do mouse rapidamente para um dos cantos da tela, caso `pyautogui.FAILSAFE` esteja habilitado.

---

## 🔒 Segurança

As credenciais do sistema **não ficam armazenadas diretamente no código**.

Elas são carregadas por meio de um arquivo `.env`, evitando a exposição de informações sensíveis no repositório.

O arquivo `.env` está listado no `.gitignore` e não deve ser enviado ao GitHub.

Foi incluído também um arquivo `.env.example` como modelo de configuração.

---

## 📚 Objetivo

Este projeto foi desenvolvido com o objetivo de praticar:

- Automação de processos (RPA);
- Automação de interfaces gráficas com PyAutoGUI;
- Manipulação de arquivos CSV utilizando Pandas;
- Organização de projetos Python;
- Boas práticas de segurança utilizando variáveis de ambiente;
- Automação de tarefas repetitivas.

---

## 📌 Melhorias Futuras

- [ ] Substituir o PyAutoGUI por Selenium ou Playwright.
- [ ] Tornar as coordenadas configuráveis.
- [ ] Criar uma interface gráfica (Tkinter ou CustomTkinter).
- [ ] Adicionar logs de execução.
- [ ] Implementar tratamento de exceções.
- [ ] Gerar relatório dos produtos cadastrados.
- [ ] Adicionar parada de automação com biblioteca keyboard.

---

## 👨‍💻 Autor

Desenvolvido por **Odirlei**.

Caso este projeto tenha sido útil para você, considere deixar uma ⭐ no repositório.
