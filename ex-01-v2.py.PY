'''
Problema:
Escreva um programa que remove a primeira ocorrencia de uma letra de uma string.
A string e a letra devem ser fornecidas pelo usuario.
'''
# ============ MODO O2 ============
# * Vou criar uma lista a partir da string, utilizando o split e join

# ============ INICIO ============

# Recebendo a string do usuário
frase = input("Digite uma frase: ")

# Recebendo a letra a ser removida
letra = input("Digite uma letra a ser removida: ")

# Criar lista --> Aqui parece que ta voltando a ser string outra vez..
# Correto??
frase = frase.split()
frase = ' '.join(frase)
print(frase)
