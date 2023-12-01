from flask import Flask, request, jsonify
from controller import gerarSenhaNormal,gerarSenhaPreferencial, cadastrarNaTabelaSenha, cadastrarUsuario, cadastrarAtendimento, listarAtendimento, cadastrarTipoAtendimento, cadastrarNaTabelaSenha, listarUsuarios, listarAtendimento, loginServidor
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

#página cadastro-usuario
@app.route('/cadastro', methods = ['POST'])
def cadastroUsuario():
    try:
        requisicao = request.get_json()

        nomeUsuario = requisicao.get('nomeUsuario')
        cpf = requisicao.get('cpf')
        assunto = requisicao.get('assunto')
        comunidade = requisicao.get('comunidade')
        preferencia = requisicao.get('preferencia')

        if preferencia == 'preferenciasim':
            senha = gerarSenhaPreferencial()
        else:
            senha = gerarSenhaNormal()


            cadastrarUsuario(cpf, nomeUsuario, comunidade)
            cadastrarNaTabelaSenha(senha)
            cadastrarTipoAtendimento(assunto)
        return jsonify({'senha': senha})  
    

    
    except Exception as e:
        return jsonify({'mensagem': 'erro'})
    
    

@app.route('/listar-atendimentos', methods =['GET'])
def listarAtendimentos():
    try:
        atendimentos = listarAtendimento()
        return jsonify({'Atendimentos': atendimentos})
    except Exception as e:
        return jsonify({'mensagem': 'erro'})   



#referentes ao servidor:

@app.route('/login-servidor', methods = ['POST'])
def login_servidor():
    try:
        cpf_servidor = request.form.get('cpf_servidor')
        senha_servidor = request.form.get('senha_servidor')

        if loginServidor(cpf_servidor, senha_servidor):
            return jsonify({'mensagem': 'Login do servidor bem-sucedido'})
        else:
            return jsonify({'mensagem': 'Login do servidor falhou'})

    except Exception as e:
        return jsonify({'mensagem': 'Erro ao processar o login do servidor'})
 







@app.route('/chamarSenha', methods =['GET'])
def chamarSenha():
   
    return "Senha convocada!"
    




if __name__ == "__main__":
    app.run()


#cadastro de senha: 
#