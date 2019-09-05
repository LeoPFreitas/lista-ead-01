'''
Problema:
* Escreva um programa que solicite ao usuário a entrada de um número inteiro
positivo ou negativo e mostre a quantidade de dígitos desse número.
'''
# Recebendo número
num1 = input("Digite um número: ")

# Eliminar sinal
if int(num1) >= 0:
    print("O número {} possui {} dígitos: ".format(num1, len(num1)))
else:
    print("O número {} possui {} dígitos: ".format(num1, len(num1)-1))
