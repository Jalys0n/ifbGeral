from flask import Flask, request, jsonify
from controller import gerarSenhaNormal,gerarSenhaPreferencial, cadastrarNaTabelaSenha, cadastrarUsuario, cadastrarAtendimento, listarAtendimento, cadastrarNaTabelaSenha, listarUsuarios, listarAtendimento, loginServidor
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

#página cadastro-usuario

@app.route('/cadastro', methods=['POST'])
def cadastroUsuario():
    try:
        requisicao = request.get_json()

        if requisicao is None:
            return jsonify({"error": "No JSON data provided"}), 400

        nome = requisicao.get('nomeUsuario')
        if nome is None:
            return jsonify({"error": "No 'nomeUsuario' provided"}), 400

        cpf_usuario = requisicao.get('cpf')
        if cpf_usuario is None:
            return jsonify({"error": "No 'cpf' provided"}), 400

        assunto = requisicao.get('assunto')
        if assunto is None:
            return jsonify({"error": "No 'assunto' provided"}), 400
            #comunidade    
        fk_tipo_usuario = requisicao.get('fk_tipo_usuario')
        if fk_tipo_usuario is None:
            return jsonify({"error": "No 'comunidade' provided"}), 400

        preferencia = requisicao.get('preferencia')
        if preferencia is None:
            return jsonify({"error": "No 'preferencia' provided"}), 400

        
        if preferencia == 'preferenciasim':
            senha = gerarSenhaPreferencial()
        else:
            senha = gerarSenhaNormal()

        cadastrarUsuario(cpf_usuario, nome, fk_tipo_usuario)
        cadastrarNaTabelaSenha(senha)
        cadastrarAtendimento(cpf_usuario, senha, 1)
        
        return jsonify({'senha': senha})

    except Exception as e:
        print(f"Erro: {str(e)}")
        return jsonify({'mensagem': f'Erro: {str(e)}'}), 400  

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
 







@app.route('/chamar-senha', methods =['GET'])
def chamarSenha():
   
    return "Senha convocada!"
    




if __name__ == "__main__":
    app.run()


#cadastro de senha: 
#

