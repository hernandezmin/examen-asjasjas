def costo_viaje(hora, tiempo, distancia):

    tarifanormal = 5.00
    preciokm = 2.50
    preciomn = 0.50

    preciototal = tarifanormal + distancia * preciokm + tiempo * preciomn
    if (hora >= 7 and hora < 9) or (hora >= 17 and hora < 19):
        recargo = preciototal * 0.20
        preciototal += recargo

    return preciototal

print("Bienvenido a Uber Guatemala")
hora = int(input("Ingrese la hora del día (en formato 24 horas, sin especificar pm o am por favor): "))
if hora > 23:
    print("Hora inválida en formato 24 horas :(, Por favor ingrese una hora entre 0 y 23.")
else:
    tiempo = float(input("Ingrese el tiempo de viaje en minutos: "))
    distancia = float(input("Ingrese la distancia recorrida en kilómetros: "))

    preciototal = costo_viaje(hora, tiempo, distancia)
    print("El costo total del viaje es: Q", preciototal)
