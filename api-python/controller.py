import random
import string
from conexao import conexao


def gerarSenhaNormal(length=6):
    letras = 'PREF'
    numeros = ''.join(random.choice(string.digits) for i in range(3)) 
    senha = letras + numeros   

    return senha

def gerarSenhaPreferencial(length=6):
   letras = 'PQM'
   numeros = ''.join(random.choice(string.digits) for i in range(3))
   senha = letras + numeros
   return senha

#table usuario
def cadastrarUsuario(cpf_usuario, nome, fk_tipo_usuario):
    cursor = conexao.cursor()
    sql = 'INSERT INTO usuarios (cpf_usuario, nome, fk_tipo_usuario) VALUES (?, ?, ?)'
    cursor.execute(sql, (cpf_usuario, nome, fk_tipo_usuario))
    conexao.commit()
    cursor.close()


def listarUsuarios():
    sql = 'SELECT * FROM usuarios'
    cursor = conexao.cursor()
    cursor.execute(sql)
    resultados = cursor.fetchall()
    cursor.close()    
    return resultados


#atendimentos 

def cadastrarAtendimento(fk_cpf_usuario, fk_idSenha, fk_tipo_atendimento):
   cursor = conexao.cursor()
   sql = 'INSERT INTO atendimentos (fk_cpf_usuario, fk_idSenha, fk_tipo_atendimento) values (?,?,?)'
   cursor.execute(sql,(fk_cpf_usuario, fk_idSenha, fk_tipo_atendimento))
   conexao.commit()
   cursor.close()      

def listarAtendimento():
   sql = 'SELECT * FROM atendimentos'
   cursor = conexao.cursor()
   cursor.execute(sql)
   resultado = cursor.fetchall()
   cursor.close()
   return resultado

   #função pra ser chamada quando terminar o atendimento
def incluirTerminoAtendimento(idSenha):
    sql = 'UPDATE atendimentos SET finalAtendimento = CURRENT_TIMESTAMP WHERE fk_idSenha = ?'
    cursor = conexao.cursor()
    cursor.execute(sql, (idSenha,))
    conexao.commit()
    cursor.close()



#senhas

def listarSenhas():
   sql = 'select idSenha from senhas'
   cursor = conexao.cursor()
   cursor.execute(sql)
   conexao.commit()
   cursor.close()


def cadastrarNaTabelaSenha(idSenha):
    sql = 'INSERT INTO senhas (idSenha, fk_status_senha) VALUES (?, 1)'
    cursor = conexao.cursor()
    cursor.execute(sql, (idSenha,))
    conexao.commit()
    cursor.close()


#assim q chamar a senha
def alterarStatus(idSenha, novoStatus):
    sql = 'UPDATE senhas SET fk_status_senha = ? WHERE idSenha = ?'
    cursor = conexao.cursor()
    cursor.execute(sql, (novoStatus, idSenha))
    conexao.commit()
    cursor.close()



#servidor:
def loginServidor(cpf_servidor, senha_servidor):
    conexao = conexao()  # Substitua pela instância real da sua classe de conexão
    servidor = conexao.executar_query("SELECT * FROM servidores WHERE cpf_servidor = %s AND senha_servidor = %s", (cpf_servidor, senha_servidor))

    if servidor:
        return True
    else:
        return False

#tabelas existentes no banco de dados: atendimento, senhas, servidores, tipo_atendimento, usuarios. ai eu acho q vai ter duas novas
#

