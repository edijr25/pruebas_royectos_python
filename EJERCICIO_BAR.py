##Un bar nos contrato para administrar el consumo de los clientes en las distintas mesas del local
##para esto debemos desarrollar un algoritomo que nos permita el ingreso de los siguientes datos de varias mesas:
##Nombre del cliente (No puede ser numero)
#La edad
#Tipo de bebida (validar cerveza limonada, gaseosa, ninguno)
##Tipo de comida (Papitas, hamburguesa, rabas, ninguno)
#Importe total

##Necesatos saber: 
#tipo de bebida mas vendida
##la edad del que pago el importe mas alto
#cuanta gente mayor de 18 años no pidió bebida

#contador por bebida
#flag edadMayor importeMayor
#contadorMayorSinBebida
#

bebidas = {"cerveza": 0, "limonada": 0, "gaseosa": 0, "ninguna": 0}
mayor_importe = 0
edad_mayor_importe = 0
mayores_sin_bebida = 0
seguir = "s"

while (seguir=="s"):
    nombre = input("Ingrese nombre: ")
    edad= int(input("Ingrese edad: "))
    while (edad <18):
        edad = int(input("Edad invalida. Reingrese edad: "))

    bebida = input("Ingrese la bebida: ")
    while (bebida != "cerveza" and bebida != "limonada" and bebida != "gaseosa" and bebida != "ninguna"):
        bebida = input("Bebida invalida, ingrese la bebida: ")

    comida = input("Ingrese la comida: ")
    while (comida != "papitas" and comida != "hamburguesas" and comida != "rabas" and comida != "ninguna"):
        comida = input("Comida invalida, ingrese la comida: ")

    importe = int(input("Importe total es: "))

    bebidas[bebida] += 1
    if importe > mayor_importe:
        mayor_importe = importe
        edad_mayor_importe = edad

    if edad > 18 and bebida == "ninguno":
        mayores_sin_bebida += 1
    
    seguir = input("Quiere continuar?: ")

# Imprimir las respuestas a las preguntas
print("Tipo de bebida más vendida:", max(bebidas, key=bebidas.get))
print("Edad del que pagó el importe más alto:", edad_mayor_importe)
print("Cantidad de mayores de 18 años que no pidieron bebida:", mayores_sin_bebida)

print("Fin del programa")