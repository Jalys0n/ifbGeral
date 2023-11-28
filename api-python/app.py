from flask import Flask
from controller import gerarSenhaNormal, gerarSenhaPreferencial
from conexao import conexao, cadastrarAtendimento, cadastrarSenha, cadastrarAtendimento, cadastrarUsuario, listarAtendimento, listarSenhasNaFila   

app = Flask(__name__)
#página cadastro-usuario
@app.route('/cadastro', methods = ['POST'])
def cadastroUsuario():
    cpf_usuario = request.form.get['cpf_usuario']
    nome = request.form.get['nomeUsuario']
    assunto = request.form.get['assuntoAtendimento']
    comunidade = request.form.get['comunidade']
    preferencia = request.form.get['preferencia']
    if preferencia == 'preferenciasim':
        senha = gerarSenhaPreferencial()
    else:
        senha = gerarSenhaNormal()
    cadastrarUsuario(cpf_usuario, nome, comunidade)
    cadastrarAtendimento()

    return ("OIIII")

@app.route('/chamarSenha', methods =['GET'])
def chamarSenha():
    for n in listarSenhasNaFila():
        print(n)
    return "Senha convocada!"
    






if __name__ == "__main__":
    app.run()


#cadastro de senha: 
#