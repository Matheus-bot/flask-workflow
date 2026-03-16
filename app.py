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
    return "Lista completa de livros da biblioteca"

@app.route("/autores")
def autores():
    return "Lista de autores cadastrados"

if __name__ == "__main__":

    app.run(debug=True)