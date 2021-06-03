#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".

def validaSim(var):
   while var not in "SsNn":
      var = input("Responda corretamente cidadão S ou N: ")
   return var

print("Eurico foi assassinado, você foi levado para o interrogatório. Responda:\n")

tel = input("Telefonou para a vítima? S/N: ")
tel = validaSim(tel)
local = input("Esteve no local do crime? S/N: ")
local = validaSim(local)
mora = input("Mora perto da vítima? S/N: ")
mora = validaSim(mora)
divida = input("Devia para a vítima? S/N: ")
divida = validaSim(divida)
trabalho = input("Já trabalhou com a vítima? S/N: ")
trabalho = validaSim(trabalho)
print() 

to_utilizando_lista = [tel, local, mora, divida, trabalho]

qtdSim = ""
for i in to_utilizando_lista:
   if i in "Ss":
      qtdSim += i
if len(qtdSim) == 2:
   print("Você foi considerado SUSPEITO, não saia da cidade.")
elif len(qtdSim) > 2 and len(qtdSim) < 5:
   print("Nossas investigações apontam que você é CÚMPLICE! Pode levar Peçanha.")
elif len(qtdSim) == 5:
   print("Senhora e senhores pegamos ele, o ASSASSINO!")
elif len(qtdSim) < 2:
   print("Tu não sabe de nada, mete o pé daqui vai! Pode marcar aí Peçanha, 'INOCENTE'.")
else: 
   print("Eu tenho cara de palhaço? Me responde direito, S ou N:")