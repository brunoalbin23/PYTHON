import numpy as np


def agrupar_de3(cadena):  #Esta funcion devuelve una lista con los caracteres agrupados de a 3
    lista = []
    sub_lista = []
    contador = 0
    for i in cadena:
        if contador == 3:
            lista.append(sub_lista)
            sub_lista = [i]
            contador = 1
        else:
            contador += 1
            sub_lista.append(i)
    while contador < 3:
        sub_lista.append(" ")
        contador += 1
    lista.append(sub_lista)
    return lista


def pasar_a_numeros(lista):
    for j in lista:
        for i in range(0, 3):
            if j[i] == " ":
                j[i] = 27
            elif j[i] == "*":
                j[i] = 28
            elif j[i] == "ñ":
                j[i] = 14
            else:
                valor = (ord(j[i]) - ord('a'))
                if valor < 14:
                    j[i] = valor
                else:
                    j[i] = valor + 1
    return lista


def encriptar(lista_numeros, T, b):
    lista_encriptada = []
    for lista in lista_numeros:  # Recorro todas las listas (de a 3)
        lista_array = np.array(lista)
        matriz_t = np.array(T)
        matriz_b = np.array(b)
        resultado = (np.dot(matriz_t, lista_array) + matriz_b) % 29
        lista_encriptada.append(resultado.tolist())
    return lista_encriptada


def pasar_a_caracter(lista):
    cadena_encriptada = ""
    for j in lista:
        for i in range(0, 3):
            if j[i] == 27:
                cadena_encriptada += " "
            elif j[i] == 28:
                cadena_encriptada += "*"
            elif j[i] == 14:
                cadena_encriptada += "ñ"
            else:
                if j[i] < 14:
                    valor = chr(j[i] + ord('a'))  # chr es igual a ord pero al revez
                else:
                    valor = chr((j[i] - 1) + ord('a'))
                cadena_encriptada += valor
    return cadena_encriptada


def letra_mas_repeticiones(lista):  # devuelve la letra mas repetida de la cadena
    contador_caracteres = {}
    for i in lista:
        for j in i:
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


def buscar_caracter(caracter, cadena):  # busca el caracter en la cadena y devuelve todas las posiciones
    posiciones = []
    for i in range(0, len(cadena) - 1):
        if cadena[i] == caracter:
            posiciones.append(i)
    return posiciones


def desencriptar(lista, T, b):
    lista_desencriptada = []
    matriz_t = np.array(T)
    inversa_t = np.linalg.inv(matriz_t)
    matriz_b = np.array(b)
    for i in lista:
        lista_array = np.array(i)
        resultado = (np.dot(inversa_t, lista_array - matriz_b)) % 29
        lista_desencriptada.append(resultado.astype(int).tolist())
    return lista_desencriptada


cadena = "colombia lo empato en el minuto noventa y seis y uruguay lo gano sacando del medio en el minuto ciento uno"

print("Cadena elegida: " + cadena)
texto_de3 = agrupar_de3(cadena)
print("Vectores de la cadena: " + str(texto_de3))

texto_numerico = pasar_a_numeros(texto_de3)
print("Vectores de la cadena en formato numerico: " + str(texto_numerico))

T = [[1, 2, 3], [0, 1, 4], [0, 0, 1]]
b = [1, 5, 2]

texto_numerico_encriptado = encriptar(texto_numerico, T, b)
print("Vectores de la cadena en formato numerico encriptados: " + str(texto_numerico_encriptado))

texto_encriptado = pasar_a_caracter(texto_numerico_encriptado)

print("\n------------- PARTE 4 ---------------\n")
letra = letra_mas_repeticiones(cadena)
posiciones = buscar_caracter(letra, cadena)
print(
    f"El caracter que mas se encuentra en la cadena original es '{letra}' y se encuentra en las posiciones: {posiciones}")

print("\n------------- PARTE 5 ---------------\n")
letra2 = letra_mas_repeticiones(texto_encriptado)
posiciones2 = buscar_caracter(letra2, texto_encriptado)
print(
    f"El caracter que mas se encuentra en la cadena encriptada es '{letra2}' y se encuentra en las posiciones: {posiciones2}")

print("\n------------- PARTE 8 ---------------\n")
# le paso la lista encriptada numerica como parametro y me devuelve (espero) la lista desenceritpada en numeros
vector_dese = desencriptar(texto_numerico_encriptado, T, b)
print("Vector desencriptado: " + str(vector_dese))
print("Cadena desencriptada: " + pasar_a_caracter(vector_dese))

