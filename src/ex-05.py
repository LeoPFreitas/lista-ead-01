'''
Problema:
* Faça um programa que recebe uma frase e retorna o número de palavras que a frase contém.
'''
# Recebendo a frase
frase = input("Digite a frae: ")

# Retornando número de palavras
frase = frase.split()
print("A entrada possui {} palavras.".format(len(frase)))
