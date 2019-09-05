'''
Problema:
* Dada uma string com uma frase informada pelo usuário (incluindo espaços em branco)
* conte a quantidade de espaços em branco 
* e a quantidade de vezes que aparecem as vogais a, e, i, o, u (separadamente).
'''

# Receber nome:
nome = input("Digite seu nome: ")

# Removendo espaçõs em branco
nomeSemEsp = ''.join(nome.split())

# Contando espaços
espacos = len(nome) - len(nomeSemEsp)

# Contando vogais
contador = 0
vogais = ['a', 'e', 'i', 'o', 'u']
for n in range(len(vogais)):
    for i in range(len(nomeSemEsp)):
        if vogais[n] == nomeSemEsp[i]:
            contador += 1

# Imprimindo na tela
print("O nome entrado é {}, ele possui {} espaços e {} vogais".format(
    nome, espacos, contador))
