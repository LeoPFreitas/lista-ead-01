'''
Problema:
* Escreva um programa que verifique se duas strings fornecidas pelo usuário são iguais 
* E mostre o total de caracteres de cada uma delas. 
* Diferencie letras maiúsculas das minúsculas.
'''
# OBS
# Não vou remover espaços com o strip nesse ex, pra ser igual por tamanho a pessoa
# não deve colocar espaço no final...nem ponto final e coisas do tipo

# Receber as duas strings
frase1 = input("Digite uma string: ")
frase2 = input("Digite outra string: ")

# Verificar igualdade
# Verificando tamanho primeiro
if len(frase1) == len(frase2):
    # Vericando letra a letra
    iguais = True
    for n in range(len(frase1)):
        if frase1[n] != frase2[n]:
            iguais = False
else:
    iguais = False

# Imprimir na tela
if iguais:
    print("A frase '{}' e '{}' são iguais".format(frase1, frase2))
else:
    print("A frase '{}' e '{}' não são iguais".format(frase1, frase2))
