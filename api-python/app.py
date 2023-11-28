from flask import Flask
from controller import gerarSenhaPreferencial,gerarSenhaNormal, cadastrarUsuario, cadastrarSenha, cadastrarAtendimento, listarSenhasNaFila, cadastrarNaTabelaSenha

app = Flask(__name__)

#página cadastro-usuario
@app.route('/solicitar-senha', methods = ['POST'])
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

    #cadastrarAtendimento tem q ser por último, preciso rever esses parâmetros! e tratar pra, caso não forem tudo, não ir nenhum. questão de atomicidade
    cadastrarAtendimento()

    if cadastrarUsuario() and cadastrarSenha() and cadastrarAtendimento():
        return "Usuário cadastrado com sucesso!"
    else:
        return "Cheque os dados e tente novamente! A senha não foi gerada"
    



#referentes ao servidor:

@app.route('/login-servidor', methods = ['POST'])
def loginServidor():
    cpf_servidor = request.form.get['cpf_servidor']
    senha_servidor = request.form.get['senha_servidor']
    loginServidor(cpf_servidor, senha_servidor)


@app.route('/chamar-senha', methods=['GET'])
def chamarSenha():
    cursor = listarSenhasNaFila()
    senha = cursor.fetchone()
    print (senha)
    cadastrarNaTabelaSenha(senha)
    cursor.close()

    return "Senha convocada!"
    




if __name__ == "__main__":
    app.run()


#cadastro de senha: 
#