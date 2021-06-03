#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar. 
# Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
from datetime import date

dados = {}

print("Faça o cadastro e descubra quando você irá se aposentar:")
nome = input("Informe seu nome: ")
nasc = int(input("Ano de nascimento - AAAA: "))
idade = date.today().year - nasc
ctps = input("Carteira de trabalho: ")

dados.update({"Nome": nome, "Nascimento": nasc, "Idade": idade, "CTPS": ctps})

if ctps != "0":
    contrat = int(input("Ano de contratação: "))
    aposentadoria = contrat + 35 - nasc 
    salario = float(input("Salário: ").replace(',', '.'))
    dados.update({"Ano de Contratação": contrat, "Salário": salario})
    
    print(("-=-"*10)+"\n-Dados do Usuário-")
    for k, v in dados.items():
        print(k,":", v)
    print(("-=-"*10)+"\nVocê se aposentará com", aposentadoria, "anos!\n"+("-=-"*10))

else:
    print(("-=-"*9)+"\n-Dados do Usuário-")
    for k, v in dados.items():
        print(k,":", v)
    print(("-=-"*9)+"\nVocê não vai se aposentar.\n"+("-=-"*9))