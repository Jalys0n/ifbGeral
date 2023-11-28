import random
import string
from conexao import conexao


def gerarSenhaNormal(length=6):
    letras = 'ABC'
    numeros = ''.join(random.choice(string.digits) for i in range(3)) 
    senha = letras + numeros   

    return senha

def gerarSenhaPreferencial(length=6):
   letras = 'PQM'
   numeros = ''.join(random.choice(string.digits) for i in range(3))
   senha = letras + numeros
   return senha

def cadastrarUsuario(cpf_usuario, nome):
    sql = 'INSERT INTO usuario (cpf_usuario,nome, origem_usuario) values (?,?,?)'
    cursor = conexao.cursor()
    cursor.execute(sql,(cpf_usuario, nome))
    conexao.commit()
    cursor.close()

def cadastrarSenha(idSenha):
    sql = 'INSERT INTO emFila (idSenha) values (?)'
    cursor = conexao.cursor()
    cursor.execute(sql, (idSenha))
    conexao.commit()
    cursor.close() 

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


def listarSenhasNaFila():
   sql = 'SELECT * FROM nafila'
   cursor = conexao.cursor()
   cursor.execute(sql)
   resultado = cursor.fetchall()
   cursor.close()


def cadastrarNaTabelaSenha(idSenha):
   sql = 'INSert into senhas (idSenha) values (?)'
   cursor = conexao.cursor()
   cursor.execute(sql)
   conexao.commit()
   cursor.close()

#tabelas existentes no banco de dados: atendimento, senhas, servidores, tipo_atendimento, usuarios. ai eu acho q vai ter duas novas
#

