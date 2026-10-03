import random

while True:
    numero = random.randint(1, 100)
    vidas = 3

    print("\n==============================")
    print("      ADIVINA EL NUMERO")
    print("==============================")
    print("He escogido un número del 1 al 100.")
    print("Tienes 3 vidas para adivinarlo.")

    while vidas > 0:
        try:
            intento = int(input("\nEscribe tu número: "))
        except ValueError:
            print("Por favor, escribe un número válido.")
            continue

        if intento == numero:
            print("¡Felicidades! ¡Adivinaste el número!")
            break

        vidas -= 1

        if intento < numero:
            print("El número es MAYOR.")
        else:
            print("El número es MENOR.")

        print("Te quedan", vidas, "vidas.")

    if vidas == 0:
        print("\n¡Perdiste!")
        print("El número era:", numero)
        print("El juego se reiniciará...")

    input("\nPresiona ENTER para comenzar una nueva ronda...")
