print("escolha o numero para tabuada")
while True:
    number = int(input("escolha o número inteiro: "))
    tabuada = int(input("até qual numero?: "))

    for i in range(tabuada, 0, -1):
     resultado = number * i
     funcao = resultado % 2
     if funcao == 0:
         print(f"a tabuada {number} * {i} = {resultado} e ele é par")
     elif funcao == 1:
         print(f"a tabuada {number} * {i} = {resultado} e ele é impar")


    continuar = input("\nPressione Enter para continuar ou digite 'sair' para encerrar: ")
    if continuar.lower() == "sair":
        print("Encerrando...")
        break
