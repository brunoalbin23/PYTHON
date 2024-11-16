def pasar_a_numeros(cadena):  #Esta funcion devuelve una lista con los valores de cada caracter
    lista_valores = []
    for i in cadena:
        if i == " ":
            lista_valores.append(27)
        elif i == "*":
            lista_valores.append(28)
        elif i == "ñ":
            lista_valores.append(14)
        else:
            valor = (ord(i) - ord('a'))  # La función old, puede tranformar letras a valores numericos con un
            if valor < 14:  # orden pero no existe la "ñ" entonces hay que mover 1 los
                lista_valores.append(valor)  # valores que le siguen en el abecedario
            else:
                lista_valores.append(valor + 1)
    return lista_valores


def criptosistema1(lista_cadena, a, b):  # Funcion que encirpta dado el a y b que queremos
    lista_encriptada = []
    for i in lista_cadena:
        lista_encriptada.append((a * i + b) % 29)
    return lista_encriptada


def pasar_a_letras(lista_encripatada):  # Pasamos de numeros a valores nuevamente para ver el mensaje encriptado
    cadena_encriptada = ""
    for i in lista_encripatada:
        if i == 27:
            cadena_encriptada += " "
        elif i == 28:
            cadena_encriptada += "*"
        elif i == 14:
            cadena_encriptada += "ñ"
        else:
            if i < 14:
                valor = chr(i + ord('a'))  # chr es igual a ord pero al revez
            else:
                valor = chr((i - 1) + ord('a'))
            cadena_encriptada += valor
    return cadena_encriptada


def letra_mas_repeticiones(cadena):
    contador_caracteres = {}
    for i in cadena:
        if i not in contador_caracteres:
            contador_caracteres[i] = 1
        else:
            contador_caracteres[i] += 1
    letra = ""
    contador = 0
    for i in contador_caracteres:
        if contador_caracteres[i] >= contador:
            letra = i
            contador = contador_caracteres[i]
    return letra


def buscar_caracter(caracter, cadena):
    posiciones = []
    for i in range(0, len(cadena) - 1):
        if cadena[i] == caracter:
            posiciones.append(i)
    return posiciones


# esta funcionan anda mal, no entiendo la logica para desencriptar una vez q este eso anda joya
def desencriptar(lista_encriptada, a, b):
    lista_desencriptada = []
    for i in lista_encriptada:
        for z in range(0, 28):
            if (i * z) % 29 == 1:
                lista_desencriptada.append(((i - b) * z) % 29)
    return lista_desencriptada


print("\n-----------------  PARTE 3  -----------------")

cadena = "colombia lo empato en el minuto noventa y seis y uruguay lo gano sacando del medio en el minuto ciento uno"

texto_pasado_numero1 = pasar_a_numeros(cadena)
texto_criptografiado = criptosistema1(texto_pasado_numero1, 5, 15)
texto_traducido1 = pasar_a_letras(texto_criptografiado)

print("Cadena que queremos encriptar: '" + cadena + "'")
print("Cadena en valores númericos: " + str(texto_pasado_numero1))
print("Cadena encriptada en valores númericos: " + str(texto_criptografiado))
print("Cadena encriptada final: '" + texto_traducido1 + "'")

print("\n-----------------  PARTE 4  -----------------")

caracter_mas = letra_mas_repeticiones(cadena)
posiciones_caracter = buscar_caracter(caracter_mas, cadena)

print("El caracter mas encontrado es: '" + caracter_mas + "'")
print(f"El caracter '{caracter_mas}' se encunetra en las posiciones: {str(posiciones_caracter)}")

print("\n-----------------  PARTE 5  -----------------")

caracter_mas_cripto1 = letra_mas_repeticiones(texto_traducido1)
posiciones_caracter_cripto1 = buscar_caracter(caracter_mas_cripto1, texto_traducido1)

print("El caracter mas encontrado es: '" + caracter_mas_cripto1 + "'")
print(f"El caracter '{caracter_mas_cripto1}' se encunetra en las posiciones: {str(posiciones_caracter_cripto1)}")

print("\n-----------------  PARTE 8  -----------------")
print(texto_pasado_numero1)
print(texto_criptografiado)
print(desencriptar(texto_criptografiado, 5, 15))
