import random

vitorias = 0
derrotas = 0
empates = 0
print("Jogo de pedra, papel e tesoura")
opcao1 = "1 - Pedra"
opcao2 = "2 - Papel"
opcao3 = "3 - Tesoura"

opcoes = ["Pedra", "Papel", "Tesoura"]

while True:

    computador = random.choice(opcoes)

    print("escolha uma das opcoes:")
    print(opcao1)
    print(opcao2)
    print(opcao3)

    resposta = int(input("escolha uma das opcoes:"))

    if resposta == 1:
        print("\nsua escolha foi: pedra")
    if resposta == 2:
        print("\nsua escolha foi: papel")
    if resposta == 3:
        print("\nsua escolha foi: tesoura")

    print(f"Computador escolheu: {computador}")

    if resposta == 1:
        if computador == "Pedra":
            print("Deu empate")
            empates += 1
        elif computador == "Papel":
            print("computador ganhou")
            derrotas += 1
        else:
            print("voce ganhou")
            vitorias += 1

    if resposta == 2:
        if computador == "Papel":
            print("Deu empate")
            empates += 1
        elif computador == "Tesoura":
            print("computador ganhou")
            derrotas += 1
        else:
            print("voce ganhou")
            vitorias += 1

    if resposta == 3:
        if computador == "Tesoura":
            print("empate")
            empates += 1
        elif computador == "Pedra":
            print("computador ganhou")
            derrotas += 1
        else:
            print("voce ganhou")
            vitorias += 1

    print(f"\nPlacar: Você: {vitorias} | Computador: {derrotas} | Empates: {empates}")

    continuar = input("\nPressione Enter para continuar ou digite 'sair' para encerrar: ")
    if continuar.capitalize() == "Sair":
        print("Encerrando...")
        break