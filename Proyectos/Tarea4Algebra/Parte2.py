def pasar_a_numeros_de3(cadena):  #Esta funcion devuelve una lista con los caracteres agrupados de a 3
    lista = []
    sub_lista =[]
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


print(pasar_a_numeros_de3("colombia lo empato en el minuto noventa y seis y uruguay lo gano sacando del medio en el minuto ciento uno"))
