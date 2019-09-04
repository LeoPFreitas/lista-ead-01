'''
Problema:
Escreva um programa que remove a primeira ocorrencia de uma letra de uma string.
A string e a letra devem ser fornecidas pelo usuario.
'''
# ============ MODO O2 ============
# * Atualizar a frase e usar o fatiamento para retirar a letra
# * Ou criar uma lista com o split, varres na lista e usar o del para remover
# * Essa segunda opção já da pra reciclar pro ex 2 ...

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
