def esPalindromo(frase):
    contador = -1
    for i in frase:
        if i != frase[contador]:
            return False
        contador -= 1
    return True


def eliminar_duplicados(lista):
    return list(set(lista))


def factorial_recursivo(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursivo(num - 1)


def suma_digitos(num):
    digitos = str(num)
    suma = 0
    for i in digitos:
        suma += int(i)
    return suma


def calculo_ocurrencia(frase):
    guardar = {}
    for i in frase:
        if i not in guardar:
            guardar[i] = 1
        else:
            guardar[i] += 1
    for i in guardar:
        print(f"El caracter '{i}' aparece {guardar[i]} veces")


def dibujar_cuadrado(lado, caracter):
    for i in range(0, lado):
        print(caracter, end=" ")
    print()
    for i in range(0, lado - 2):
        for j in range(1, lado + 1):
            if j == 1:
                print(caracter, end=" ")
            elif j == lado:
                print(caracter)
            else:
                print(" ", end=" ")
    for i in range(0, lado):
        print(caracter, end=" ")


def numeros_primos(num):
    primos = []
    if num >= 2:
        primos.append(2)
    for i in range(3, num + 1):
        es_primo = True
        for j in range(2, i + 1):
            if i % j == 0 and i != j:
                es_primo = False
                break
        if es_primo:
            primos.append(i)
    return primos


# print(esPalindromo("ala"))
# print(eliminar_duplicados(["apple", "banana", "cherry", "cherry", "pera", "banana", "anana"]))
# print(factorial_recursivo(5))
# print(suma_digitos(5465))
# calculo_ocurrencia("hola como estas jajajjaa")
# dibujar_cuadrado(5, "*")
# print(numeros_primos(50))
