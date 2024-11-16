def pasar_a_numeros(cadena):  #Esta funcion devuelve una lista con los valores de cada caracter referenciado a la letra del obligatorio
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


def criptosistema1(lista_cadena, a, b):
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


def letra_mas_repeticiones(cadena):          # devuelve la letra mas repetida de la cadena
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


def buscar_caracter(caracter, cadena):   # busca el caracter en la cadena y devuelve todas las posiciones
    posiciones = []
    for i in range(0, len(cadena) - 1):
        if cadena[i] == caracter:
            posiciones.append(i)
    return posiciones


def desencriptar(lista_encriptada, a, b):
    lista_desencriptada = []
    for i in lista_encriptada:
        for z in range(0, 28):
            if (z * a) % 29 == 1:
                lista_desencriptada.append((z * (i - b)) % 29)
    return lista_desencriptada


print("\n-----------------  PARTE 3  -----------------")

cadena = "colombia lo empato en el minuto noventa y seis y uruguay lo gano sacando del medio en el minuto ciento uno"

texto_pasado_numero = pasar_a_numeros(cadena)
texto_criptografiado = criptosistema1(texto_pasado_numero, 5, 15)
texto_traducido = pasar_a_letras(texto_criptografiado)

print("Cadena que queremos encriptar: '" + cadena + "'")
print("Cadena en valores númericos: " + str(texto_pasado_numero))
print("Cadena encriptada en valores númericos: " + str(texto_criptografiado))
print("Cadena encriptada final: '" + texto_traducido + "'")

print("\n-----------------  PARTE 4  -----------------")

caracter_mas = letra_mas_repeticiones(cadena)
posiciones_caracter = buscar_caracter(caracter_mas, cadena)

print("El caracter mas encontrado es: '" + caracter_mas + "'")
print(f"El caracter '{caracter_mas}' se encunetra en las posiciones: {str(posiciones_caracter)}")

print("\n-----------------  PARTE 5  -----------------")

caracter_mas_cripto = letra_mas_repeticiones(texto_traducido)
posiciones_caracter_cripto = buscar_caracter(caracter_mas_cripto, texto_traducido)

print("El caracter mas encontrado es: '" + caracter_mas_cripto + "'")
print(f"El caracter '{caracter_mas_cripto}' se encunetra en las posiciones: {str(posiciones_caracter_cripto)}")

print("\n-----------------  PARTE 8  -----------------")
print(texto_pasado_numero)
print(texto_criptografiado)
print(desencriptar(texto_criptografiado, 5, 15))  #Chequeamos que es igual a el texto_pasado_numero
print(pasar_a_letras(desencriptar(texto_criptografiado, 5, 15)))
