'''
Problema:
* Faça um programa que solicite o nome do usuário 
* Imprima-o na vertical e em formato de escada. Ex.:
    l
    le
    leo
'''
# Recebendo o nome
nome = input("Digite seu nome: ")

# Imprimindo em escada
for i in range(len(nome)):
    print(nome[:i+1])
