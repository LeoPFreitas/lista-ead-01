'''
Problema:
* Escreva um programa que remove todas as ocorrências de uma letra de uma string.
* A string e a letra devem ser fornecidas pelo usuário.
'''

# Recebendo a string e a letra
frase = input("Digite uma frase: ")
letra = input("Digite uma letra a ser removida: ")

# Armazenar frase original
fraseOriginal = frase

# Gerando lista
frase = frase.split()

# Remover letra da palavra e atualizar a lista frase
for n in range(len(frase)):
    palavra = frase[n]
    for i in range(len(palavra)-1):
        if (letra == palavra[i]):
            palavra = palavra[:i] + palavra[i+1:]
    frase[n] = palavra

# Usar o join para torna em string outra vez
frase = ' '.join(frase)

# Printar na tela resultado
print("A frase original era '{}' e a frase com a remoção da letra '{}' é '{}'.".format(
    fraseOriginal, letra, frase))
