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

