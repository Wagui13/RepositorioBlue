#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. 
# Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.

def vogalConsoante(frase):
    qtdVogal, qtdConsoante = "", ""
    for i in frase:
        if i.lower() in "aáàâãeéèêiíïoóôõöuú":
            qtdVogal += i     
        elif i.lower() in "bcdfghjklmnpqrstvwxyz": 
            qtdConsoante += i
    return qtdVogal, qtdConsoante    

frase = input("Digite uma frase e veja quantas vogais e consoantes ela tem:\n")
vog, conso = vogalConsoante(frase)

print(f"Sua frase contém {len(vog)} vogais:", vog) 
print(f"Sua frase contém {len(conso)} consoantes:", conso)