import random

minusculas = "abcdefghijklmnopqrstuvwxyzñ"
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZÑ"
numeros = "1234567890"
simbolos = "(){}[]*·:;/-_"

todos = minusculas + mayusculas + numeros + simbolos

dim = 16

clave = "".join(random.sample(todos,dim))
print (clave)