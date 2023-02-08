import random

def jogar():

    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1, 101)

    total_tentativas = 0
    total_chutes = 1
    pontos = 1000

    print("Escolha uma dificuldade")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input(""))


    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    elif nivel == 3:
        total_tentativas = 5

    for total_chutes in range(1,total_tentativas + 1):
        chute_str = input("Escreva um valor entre 1 e 100: ")
        chute = int(chute_str)

        print("Tentativa {} de {}".format(total_chutes, total_tentativas))
        print("Voce chutou", chute)

        if chute < 1 or chute > 100:
            print("Você deve chutar um valor entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Voce acertou")
            print("Você fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Voce errou! Voce chutou um numero maior que o numero secreto")
            if menor:
                print("Voce errou! Voce chutou um numero menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo")
    print("O numero secreto era {}".format(numero_secreto))

if __name__ == "__main__":
    jogar()

    
