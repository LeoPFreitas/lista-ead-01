'''
Problema:
* Faça um programa que permita ao usuário digitar o seu nome
* e em seguida o mostre de trás para frente utilizando somente letras maiúsculas.
'''

# Recebendo nome
nome = input("Digite sseu nome: ")

# Imprimir invertido em maiúsculo
nome = nome.upper()
print(nome[::-1])
