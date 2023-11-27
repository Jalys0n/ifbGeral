import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    password = 'Odekomorode2',
    database = 'registrodeatendimentora'
     )
if db:
 print ("Conectado com sucesso!")
else:
 print ("Não foi possível conectar.")

def cadastroUsuario():
    sql = 'INSERT INTO usuario (cpf_usuario,nome) values (?,?)'

def cadastroSenha():
    sql = 'INSERT INTO senha (idSenha) values (?)'

def cadastroAtendimento():
   sql = 'INSERT INTO atendimento (comecoAtendimento, guiche, fk_cpf_usuario, fk_tipo_atendimento, fk_cpf_servidor, fk_idSenha)'     

def    



#tabelas existentes no banco de dados: atendimento, senhas, servidores, tipo_atendimento, usuarios