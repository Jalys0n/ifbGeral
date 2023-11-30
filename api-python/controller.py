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

def cadastrarUsuario(cpf_usuario, nome, comunidade):
    sql = 'INSERT INTO usuario (cpf_usuario,nome, origem_usuario) values (?,?,?)'
    cursor = conexao.cursor()
    cursor.execute(sql,(cpf_usuario, nome))
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

def cadastrarAtendimento(guiche, fk_cpf_usuario, fk_cpf_servidor, fk_idSenha):
   sql = 'INSERT INTO atendimento (guiche, fk_cpf_usuario, fk_cpf_servidor, fk_idSenha)'
   cursor = conexao.cursor()
   cursor.execute(sql, (guiche, fk_cpf_usuario, fk_cpf_servidor, fk_idSenha))
   conexao.commit()
   cursor.close()      

def listarAtendimento():
   sql = 'SELECT * FROM atendimento'
   cursor = conexao.cursor()
   cursor.execute(sql)
   resultado = cursor.fetchall()
   cursor.close()
   return resultado

   #função pra ser chamada quando terminar o atendimento
def incluirTerminoAtendimento(idSenha):
   sql = 'insert into atendimento (finalAtendimento) where idSenha = ?'
   cursor = conexao.cursor()
   cursor.execute(sql, (idSenha))
   cursor.close()   

def cadastrarTipoAtendimento(tipoAtendimento):
   sql = 'insert into tipo_atendimento (tipoAtendimento) values (?)'
   cursor = conexao.cursor()
   cursor.execute(sql,(tipoAtendimento))
   cursor.close()

#senhas

#def listarSenhasNaFila():
 #  sql = 'SELECT * FROM nafila'
  # cursor = conexao.cursor()
  # cursor.execute(sql)
  # resultado = cursor.fetchall()
  # cursor.close()


def cadastrarNaTabelaSenha(idSenha):
   sql = 'INSert into senhas (idSenha) values (?)'
   cursor = conexao.cursor()
   cursor.execute(sql)
   conexao.commit()
   cursor.close()

def cadastrarSenha(idSenha):
    sql = 'INSERT INTO emFila (idSenha) values (?)'
    cursor = conexao.cursor()
    cursor.execute(sql, (idSenha))
    conexao.commit()
    cursor.close() 


#tabelas existentes no banco de dados: atendimento, senhas, servidores, tipo_atendimento, usuarios. ai eu acho q vai ter duas novas
#

