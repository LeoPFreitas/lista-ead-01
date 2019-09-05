'''
Problema:
* Escreva um programa que reconhece se uma string é um palíndromo. 
* Considere letras maiúsculas e minúsculas como sendo iguais. Exemplo: Arara, ovO, reter.
'''

# Receber sring
fraseOriginal = input("Digite uma sring: ")

# Converter tudo para minúsculo
frase = fraseOriginal.lower()

# Verificar se é palíndromo
if frase[::1] == frase[::-1]:
    print("A string {} é palíndroma.".format(fraseOriginal))
else:
    print("A string {} não é palíndroma.".format(fraseOriginal))
