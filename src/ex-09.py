'''
Problema:
* Um anagrama é uma palavra que é feita a partir da transposição 
* das letras de outra palavra ou frase. 
* Por exemplo, “Iracema” é um anagrama para “America”. 
* Escreva um programa que decida se uma string é um anagrama de outra string, 
* ignorando os espaços em branco. 
* O programa deve considerar maiúsculas e minúsculas como sendo caracteres 
* iguais, ou seja, “a” = “A”.
'''
# Receber a palavra e string
palavra = input("Digite uma palavra ou frase: ")
anagrama = input("Digite o possível anagrama para checagem: ")

# guardar original
palOrig = palavra
anaOrig = anagrama

# Deixar tudo minúsculo
palavra = palavra.lower()
anagrama = anagrama.lower()

# Eliminando espaços
palavra = ''.join(palavra.split())
anagrama = ''.join(anagrama.split())

# Verificar se é anagrama
checagem = True
if len(palavra) != len(anagrama):
    checagem = False
else:
    # Gerar listas
    listaPalavra = []
    listaAnagrama = []
    for n in range(len(palavra)):
        listaPalavra.append(palavra[n])
        listaAnagrama.append(anagrama[n])

    # Ordenar listas
    listaAnagrama.sort()
    listaPalavra.sort()

    # Conferir igualdade
    if listaPalavra == listaAnagrama:
        checagem = True
    else:
        checagem = False

# Imprimir na tela
if checagem:
    print("A palavra/frase '{}' é anagrama de '{}'".format(palOrig, anaOrig))
else:
    print("A palavra/frase '{}' não é anagrama de '{}'".format(palOrig, anaOrig))
