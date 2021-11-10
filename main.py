from random import randint
pergunta = str(input("Você gostaria de jogar o dado? "))
if pergunta == "sim":
        d = randint(1,6)
        print(d)
        pergunta2 = str(input("Você quer jogar o dado novamente? "))
        while True:
            if pergunta2 == "sim":
                d = randint(1, 6)
                print(d)
                pergunta2 = str(input("Você quer jogar o dado novamente? "))
            else:
                print("O jogo acabou")
                break
else:
    print("Digite sim, se não o programa não vai funcionar")