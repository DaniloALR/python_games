import forca
import adivinhacao

def escolhe_jogo():
    print("********************************")
    print("******* Escolha um jogo! *******")
    print("********************************")

    print("(1) Forca (2) Adivinhacao ")
    jogo = int(input(""))

    if jogo == 1:
        print("Voce iniciou forca")
        forca.jogar()
    elif jogo == 2:
        print("Voce iniciou adivinhacao")
        adivinhacao.jogar()

if __name__ == "__main__":
    escolhe_jogo()