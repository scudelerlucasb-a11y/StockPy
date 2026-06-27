vogal = ["a", "e", "i", "o", "u"]
while True:
    nome = input("Digite uma palavra:")
    contador = 0
    for letra in nome:
        if letra in vogal:
            contador +=1

    print(f"a palavra {nome} tem {contador} vogais")

    continuar = input("\nPressione Enter para continuar ou digite 'sair' para encerrar: ")
    if continuar.capitalize() == "Sair":
            print("Encerrando...")
            break


