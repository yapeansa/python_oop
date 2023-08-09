#!/bin/python3

import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0

    print('Qual o nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina o nível: '))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    pontos = 1000

    for rodada in range(1, total_de_tentativas + 1):

        print(f'Tentativa {rodada} de {total_de_tentativas}')
        chute_str = input("Digite um número de 1 a 100: ")
        print(f'Você digitou {chute_str}')

        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print('Você deve digitar um número de 1 a 100')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto

        if (acertou):
            print(f'Você acertou e fez {pontos}!')
            break
        else:
            if (maior):
                print(f'Você errou! O número secreto é menor do que {chute}')
            else:
                print(f'Você errou! O número secreto é maior do que {chute}')
            pontos_perdidos = round(abs(numero_secreto - chute) / 3)
            pontos -= pontos_perdidos

    print('Fim do jogo.')

if (__name__ == '__main__'):
    jogar()
