#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. 
   # Se não, mostre que a multiplicação não foi maior que 40.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1+num2
print(f"\nA soma de {num1} + {num2} é igual a {soma}")
mult = num1*num2
print(f"A multiplicação de {num1} * {num2} é igual a {mult}")
div = num1//num2
print(f"A divisão inteira de {num1} / {num2} é igual a {div}")

if num1 > num2:
    print(f"{num1} é maior que {num2}")
else: 
    print(f"{num2} é maior que {num1}")

if soma % 2 == 0:
    print(f"O número {soma} resultado da soma, é par.")
else:  
    print(f"O número {soma} resultado da soma, é impar.")

if mult > 40:
    if div == 0:
        print("Divisão por zero não rola amigão.")
    else:
        print(f"Resultado da Multiplicação: {mult}, divido pelo resultado da Divisão Inteira: {div}, é igual a {mult/div}")
else:
    print(f"A multiplicação é menor que 40.")