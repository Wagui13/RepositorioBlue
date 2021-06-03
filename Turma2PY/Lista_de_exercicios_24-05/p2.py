#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string 
# com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, 
# depois mostre na tela essa mesma frase sem nenhuma vogal.

frase = input("Digite uma frase e veja quantas vogais e consoantes ela tem:\n")
print()

qtdVogal, qtdConsoante = "", ""
for i in frase:
    if i.lower() in "aáàâãeéèêiíïoóôõöuú":
        qtdVogal += i     
    elif i.lower() in "bcçdfghjklmnpqrstvwxyz": 
        qtdConsoante += i    

print(f"Sua frase contém {len(qtdVogal)} vogais:", qtdVogal) 
print(f"Sua frase contém {len(qtdConsoante)} consoantes:", qtdConsoante)