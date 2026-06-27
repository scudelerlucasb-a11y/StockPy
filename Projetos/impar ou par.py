print("se é impar ou par")

number = int(input("digite um numero inteiro: "))
resultado = number % 2

if resultado == 0:
    print(f"seu numero é par \n {number}")

elif resultado == 1:
    print(f"seu numero é impar \n {number}")