from flask import Flask, request, jsonify
from controller import gerarSenhaNormal,gerarSenhaPreferencial, cadastrarUsuario, cadastrarSenha, cadastrarAtendimento, listarAtendimento, cadastrarTipoAtendimento, cadastrarNaTabelaSenha, listarUsuarios, listarAtendimento
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
            cadastrarSenha(senha)
            cadastrarTipoAtendimento(assunto)
        return jsonify({'senha': 'senha'})  
    

    
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

#@app.route('/loginServidor', methods = ['POST'])
#def loginServidor():
 #   cpf_servidor = request.form.get['cpf_servidor']
  #  senha_servidor = request.form.get['senha_servidor']
   # loginServidor(cpf_servidor, senha_servidor)







@app.route('/chamarSenha', methods =['GET'])
def chamarSenha():
   
    return "Senha convocada!"
    




if __name__ == "__main__":
    app.run()


#cadastro de senha: 
#