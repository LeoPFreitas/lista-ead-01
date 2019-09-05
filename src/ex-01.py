'''
Problema:
Escreva um programa que remove a primeira ocorrencia de uma letra de uma string.
A string e a letra devem ser fornecidas pelo usuario.
'''

# Recebendo a string do usuário
frase = input("Digite uma frase: ")

# Recebendo a letra a ser removida
letra = input("Digite uma letra a ser removida: ")

# Removendo a letra
indice = 0
encontrou = False

while (indice < len(frase)) and (not encontrou):
    if (letra == frase[indice]):
        encontrou = True
    else:
        indice += 1

# Imprimindo
if encontrou:
    fraseFinal = frase[0:indice] + frase[indice+1:]
    print("A frase original é '{}' e a frase com a letra '{}' removida é '{}'".format(
        frase, letra, fraseFinal))
else:
    print("A letra {} não ocorre na frase {}".format(letra, frase))
