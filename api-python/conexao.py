import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    password = 'Odekomorode2',
    database = 'registrodeatendimentora'
     )
if conexao:
 print ("Conectado com sucesso!")
else:
 print ("Não foi possível conectar.")

def cadastrarUsuario(cpf_usuario, nome):
    sql = 'INSERT INTO usuario (cpf_usuario,nome, comunidade) values (?,?,?)'
    cursor = conexao.cursor()
    cursor.execute(sql,(cpf_usuario, nome))
    conexao.commit()
    cursor.close()

def cadastrarSenha(idSenha):
    sql = 'INSERT INTO senha (idSenha) values (?)'
    cursor = conexao.cursor()
    cursor.execute(sql, (idSenha,))
    conexao.commit()
    cursor.close() 

def cadastrarAtendimento(comecoAtendimento, guiche, fk_cpf_usuario, fk_cpf_servidor, fk_idSenha):
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

#tabelas existentes no banco de dados: atendimento, senhas, servidores, tipo_atendimento, usuarios