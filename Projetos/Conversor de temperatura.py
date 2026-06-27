print("Conversor de temperatura")

opcao1 = "1- Celsius para Fahrenheit"
opcao2 = "2 - Fahrenheit para Celsius"
while True:
    print(opcao1)
    print(opcao2)
    resposta = int(input("Escolha uma opção:"))
    valor = float(input("Digite a temperatura:"))

    F = (valor * 9 / 5) + 32
    C = (valor - 32) * 5 / 9

    if resposta == 1:
        print(f"{valor}°C = {F:.2f}°F")
    elif resposta == 2:
        print(f"{valor}°F = {C:.2f}°C")
    else:
        print("invalido")

    continuar = input("\nPressione Enter para continuar ou digite 'sair' para encerrar: ")
    if continuar.capitalize() == "Sair":
            print("Encerrando...")
            break






