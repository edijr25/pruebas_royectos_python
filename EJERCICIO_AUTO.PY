##Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de
##autos que tienen disponible a la venta. Para esto se necesita saber de cada auto: la
##marca, el año del modelo y el precio (validar los tipos de datos ingresados) y
##mostrarlos por pantalla en forma secuencial y ordenada.


# Definimos la lista vacía para almacenar la información de los autos
autos = []

# Pedimos la información de cada auto al usuario y la agregamos a la lista
for i in range(2):
    marca = input(f"Ingrese la marca del auto {i+1}: ")
    while True:
        try:
            anio = int(input(f"Ingrese el año del modelo del auto {i+1}: "))
            break
        except ValueError:
            print("Error: Ingrese un año válido.")
    while True:
        try:
            precio = float(input(f"Ingrese el precio del auto {i+1}: "))
            break
        except ValueError:
            print("Error: Ingrese un precio válido.")
    
    autos.append({"marca": marca, "anio": anio, "precio": precio})

# Ordenamos la lista de autos por año del modelo
autos.sort(key=lambda x: x["anio"])

# Mostramos la información de los autos en orden secuencial
print("Información de los autos:")
for auto in autos:
    print(f"Marca: {auto['marca']}, Año del modelo: {auto['anio']}, Precio: {auto['precio']}")
