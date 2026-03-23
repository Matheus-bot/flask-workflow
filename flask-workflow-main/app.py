from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Sistema de Gerenciamento de Biblioteca"

@app.route("/sobre")
def sobre():
    return "Projeto da disciplina de CI/CD"

@app.route("/livros")
def livros():
    return "Lista completa de livros da biblioteca

@app.route("/autores")
def autores():
    return "Lista completa de autores"

@app.route("/contato")
def contato():
    return "Página de contato"


@app.route("/cadastro-livro")
def cadastro_livro():
    return "Formulário de cadastro de livros"

if __name__ == "__main__":

    app.run(debug=True)