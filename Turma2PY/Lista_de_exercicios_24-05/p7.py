#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que 
# mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.0
numeros = [[],[]]

for i in range(7):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        numeros[0].append(num)
    else: 
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()
print(numeros)