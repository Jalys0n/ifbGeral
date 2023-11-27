import random
import string
from conexao import db

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

