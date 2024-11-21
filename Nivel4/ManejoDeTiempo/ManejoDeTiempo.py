from datetime import datetime, timedelta


class ManejoDeTiempo:

    def saber_dias_vividos(self):

        fecha_actual = datetime.now()

        print("Ahora ingrese la fecha de su nacimiento (en formato númerico)")

        while True:
            dia = str(input("Dia: "))
            mes = str(input("Mes: "))
            ano = str(input("Año: "))
            if self.validar_fecha(dia, mes, ano):
                break
            print("Fecha invalida o formato no correspondiente, pofavor intente denuevo")

        fecha_nacimiento = datetime(int(ano), int(mes), int(dia))
        dias_vividos = (fecha_actual-fecha_nacimiento).days

        print(f"Si naciste en la fecha {dia}/{mes}/{ano} has vivido {dias_vividos} días hasta la fecha")

    def validar_fecha(self, dia, mes, ano):

        if not dia.isnumeric() or not mes.isnumeric() or not ano.isnumeric():
            return False

        dia = int(dia)
        mes = int(mes)
        ano = int(ano)

        # Lo voy a hacer para numeros entre 0 y 3000 ya q no tiene mucho sentido otro je
        if 3000 < ano or ano < 0:
            return False
        else:
            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                if 0 < dia <= 31:
                    return True
            elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                if 0 < dia <= 30:
                    return True
            elif mes == 2 and 0 < dia <= 28:
                return True
            elif self.ano_bisiesto(ano) and mes == 2 and 29 >= dia > 0:
                return True
            else:
                return False

    def ano_bisiesto(self, ano):
        if ano % 400 == 0:
            return True
        elif ano % 4 == 0 and ano % 100 != 0:
            return True
        else:
            return False
