#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma string 
# no formato D de mesPorExtenso de AAAA. Valide a data e retorne NULL caso a data seja inválida.
from datetime import datetime, date

def formataData(data_n):
    try:
        data = datetime.strptime(data_n, "%d/%m/%Y")
        print(data.strftime("%d %B %Y").upper()) #Não sei se era exatamente isso
    except:
        print("\nData Inválida!")

data_n = input("Sua data de nascimento, por gentileza - DD/MM/AAAA: ")
formataData(data_n)