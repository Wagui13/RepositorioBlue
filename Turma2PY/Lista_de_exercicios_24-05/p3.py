#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu 
# processamento, só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a 
# seu usuário e apresente a ele o jogo da advinhação, onde o computador vai “pensar” em um número inteiro entre 0 e 20. 
# O jogador vai tentar adivinhar qual número foi escolhido até acertar, a cada palpite do usuário diga a ele 
# se o número escolhido pelo computador é maior ou menor ao que ele palpitou, no final mostre quantos palpites 
# foram necessários para vencer.
import random

nome = input("Olá Pessoa! Bem vindo(a) ao execício 03.\nPor favor digite o seu nome para que eu possa completa-lo: ")
senha = input("Digite a senha: ")

while senha != "1234":
    senha = input("Pelamor de deus, você tá vendo a senha ali código: ")
print(f"\nCerto {nome}! Boas vindas!\nAgora vamos brincar de jogo da advinhação.\nAcerte o número sorteado pelo computador:")

while True:
    pc = random.randint(0,20)
    player = int(input("Um número, meu anjo: "))
    if player < pc:
        print("O número escolhido pelo computador é maior!\n")
    elif player > pc:
        print("O número escolhido pelo computador é menor!\n")
    else:
        print(f"Parabéns {nome}, você acertou!")
        break