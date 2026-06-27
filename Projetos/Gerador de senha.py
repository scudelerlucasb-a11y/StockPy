import random
letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%^&*."

while True:
    quantidade = int(input("Quantos caracteres sua senha?(minimo 8) "))
    quantidade_senhas = int(input("Quantas senhas? "))
    caracteres = simbolos + letras + numeros

    if quantidade >= 8:
        for i in range(quantidade_senhas):
            senha = []
            for j in range(3):
                senha.append(random.choice(simbolos))
            for j in range(3):
                senha.append(random.choice(numeros))
            for j in range(quantidade - 6):
                senha.append(random.choice(caracteres))
            random.shuffle(senha)
            print(f"Senha {i + 1}: {''.join(senha)}")
    else:
        print("Senha fraca! Digite pelo menos 8 caracteres.")

    continuar = input("\nPressione Enter para criar outra senha ou digite 'sair' para encerrar: ")
    if continuar.capitalize() == "Sair":
        print("Encerrando...")
        break