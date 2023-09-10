#LISTAS

frutas =['manzana', 'pera', 'fresa', 'mandarina', 'mango']
print(f"la primera fruta es: {frutas[0]} \ny la última fruta es: {frutas[4]}")

frutas.append("guanabana")
print(frutas)

frutas.insert(2,"naranja")
print(frutas)

#Crear una lista de números y calcular la suma de todos los números en la lista.
numeros = [1,2,3,4,20,30,15]
# Inicializar una variable para almacenar la suma
suma = 0
# Recorrer la lista y sumar cada número
for numero in numeros:
    suma += numero

# Imprimir el resultado
print("La suma de los números en la lista es:", suma)

#TUPLAS

#count este metodo devuelve la cantidad de veces que aparece el elemento en la tupla

profesores = ('Luis','santiago','duvan', 'luis', 'andres', 'santiago', 'duvan', 'duvan')
print('La cantidad de duvan que aparece son:', profesores.count('duvan'))
print(f"La cantidad de duvan que aparece son: {profesores.count('duvan')}")

#Crear una tupla con tus tres colores favoritos y mostrarlos en la pantalla uno por uno.

colores = ('amarillo', 'azumadrado', 'enrojecido')
print(colores[0])
print(colores[1])
print(colores[2])

# Mostrar cada color en la tupla uno por uno
for color in colores:
    print(color)

#DICCIONARIO
#Crear un diccionario con las capitales de tres países y luego imprimir la capital de un país especificado por el usuario.
capitales ={
    'España':'Barcelona',
    'Bogota': 'Colombia', 
    'Chile': 'Santiago',
    'Quenia': 'Nairobi'
}

print(capitales)
print(capitales["Chile"])

capitales['Quenia']="Sinsinati"
print(capitales)
capitales["Canada"]="Otawa"
print(capitales)

for paises, ciudades in capitales.items():
    print(f"El pais es:{paises} y su capital es: {ciudades}")
    