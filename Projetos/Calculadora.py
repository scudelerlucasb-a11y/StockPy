while True:
    number1 = float(input("Primeiro número: "))
    number2 = float(input("Segundo número: "))
    number3 = float(input("Terceiro número: "))

    print("Opções:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao = input("Escolha uma das opções: ")

    if opcao == "1":
        print("Resultado:", number1 + number2 + number3)
    elif opcao == "2":
        print("Resultado:", number1 - number2 - number3)
    elif opcao == "3":
        print("Resultado:", number1 * number2 * number3)
    elif opcao == "4":
        print("Resultado:", number1 / number2 / number3)
    else:
        print("Opção inválida!")

    continuar = input("\nPressione Enter para continuar ou digite 'sair' para encerrar: ")
    if continuar.lower() == "sair":
        print("Encerrando...")
        break