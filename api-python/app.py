from flask import Flask
from controller import gerarSenhaNormal, gerarSenhaPreferencial
from conexao import db

app = Flask(__name__)


@app.route("/cadastro")
def hello_world():
    password = gerarSenhaNormal()
    senha = gerarSenhaPreferencial()
    print("Senha normal:", password)
    print("Prefencial:", senha)
    
    return "Senha gerada. Consulte o terminal para visualizá-la."








if __name__ == "__main__":
    app.run()


#cadastro de senha: 
#