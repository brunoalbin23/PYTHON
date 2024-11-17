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


texto_de3 = agrupar_de3(
    "colombia lo empato en el minuto noventa y seis y uruguay lo gano sacando del medio en el minuto ciento uno")
texto_de3_numerico = pasar_a_numeros(texto_de3)

print(texto_de3_numerico)
