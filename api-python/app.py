from flask import Flask
from controller import gerarSenhaNormal, cadastrarUsuario, cadastrarSenha, cadastrarAtendimento, listarAtendimento, listarSenhasNaFila, cadastrarNaTabelaSenha

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
    cadastrarSenha(senha)

    #cadastrarAtendimento tem q ser por último, preciso rever esses parâmetros!
    cadastrarAtendimento()

    if cadastrarUsuario() and cadastrarSenha() and cadastrarAtendimento():
        return "Usuário cadastrado com sucesso!"
    else:
        return "Cheque os dados e tente novamente! A senha não foi gerada"
    





#referentes ao servidor:

@app.route('/loginServidor', methods = ['POST'])
def loginServidor():
    cpf_servidor = request.form.get['cpf_servidor']
    senha_servidor = request.form.get['senha_servidor']
    loginServidor(cpf_servidor, senha_servidor)


@app.route('/chamarSenha', methods =['GET'])
def chamarSenha():
    for n in listarSenhasNaFila():
        print(n)

    #fazer um if porque ai, quando estiver feita, mandar essa senha pra tabela senhas ok!
    

    return "Senha convocada!"
    




if __name__ == "__main__":
    app.run()


#cadastro de senha: 
#