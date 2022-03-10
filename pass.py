import random

#Dim (password length)
#sim (boolean simbols)
def passRandom(dim, sim):
    minusculas = "abcdefghijklmnopqrstuvwxyzñ"
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZÑ"
    numeros = "1234567890"
    simbolos = "(){}[]*·:;/-_"

    if sim: #password with simbols
        todos = minusculas + mayusculas + numeros + simbolos
    else:   #password withouth simbols
        todos = minusculas + mayusculas + numeros
    
    clave = "".join(random.sample(todos,dim))
    return clave

print (passRandom(5, False))

