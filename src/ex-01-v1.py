'''
Problema:
Escreva um programa que remove a primeira ocorrencia de uma letra de uma string.
A string e a letra devem ser fornecidas pelo usuario.
'''
# ============ MODO O1 ============
# * REMOÇÃO POR FATIAMENTO
# * Neste modo, foi utilizado a string frase e não houve como remover com o del...
#   seria por ela (frase) não ser uma lista????
# * Eu utilizei a fatiamento para não imprimir a letra, mas ela não foi excluida
#   da string de fato.

# ============ EM ABERTO ============
# * Utilizar método para colocar tudo em minúsculo e evitar o problema de letra
#   minúscula na verificxação

# ============ IMPORTANTE ============
# * VERSÃO 01 DESTE PROBLEMA, VER V2 PARA VERSÃO 02

# ============ INICIO ============

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
    print("A frase original é '{}' e a frase com a letra removida é '{}'".format(
        frase, frase[0:indice]+frase[indice+1:]))
else:
    print("A letra {} não ocorre na frase {}".format(letra, frase))
