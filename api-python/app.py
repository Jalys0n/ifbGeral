from flask import Flask, request, jsonify
from controller import gerarSenhaNormal,gerarSenhaPreferencial, cadastrarUsuario, cadastrarSenha, cadastrarAtendimento, listarAtendimento, cadastrarTipoAtendimento, listarSenhasNaFila, cadastrarNaTabelaSenha
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

#página cadastro-usuario
@app.route('/cadastro', methods = ['POST'])
def cadastroUsuario():
    try:
        data = request.get_json()
        
        
        nomeUsuario = data['nomeUsuario']
        cpf = data['cpf']
        assunto = data['assunto']
        comunidade = data['comunidade']
        preferencia = data['preferencia']

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