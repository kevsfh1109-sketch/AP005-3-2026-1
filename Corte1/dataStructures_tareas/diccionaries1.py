# Diccionario con sensores y sus valores de temperatura
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}

# Diccionario con número de cámaras en distintas ubicaciones
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

# Imprime el diccionario de sensores
print(sensors)

# Imprime el diccionario de cámaras
print(num_cameras)

# Diccionario con traducciones de palabras
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

# Imprime el diccionario de traducciones
print(translations)


## Verificando un error:

# Diccionario inválido (las listas no pueden ser claves porque son mutables)
powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}

# Intenta imprimir el diccionario (esto causaría error)
print(powers)


# Diccionario con familias y sus hijos
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}

# Imprime el diccionario de hijos
print(children)


# Crea un diccionario vacío
my_empty_dictionary = {}

# Imprime el diccionario vacío
print(my_empty_dictionary)


# Diccionario con menú y precios
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

# Imprime el menú antes de modificarlo
print("Before: ", menu)

# Agrega un nuevo elemento al diccionario
menu["cheesecake"] = 8

# Imprime el menú después de agregar el nuevo elemento
print("After", menu)


# Diccionario con animales en el zoológico
animals_in_zoo = {"dinosaurs": 0}

# Se vuelve a asignar el diccionario (sobrescribe el anterior)
animals_in_zoo = {"dinosaurs": 0}

# Se sobrescribe nuevamente con otro valor
animals_in_zoo = {"horses": 2}

# Imprime el diccionario final
print(animals_in_zoo)


## Agregar múltiples claves

# Diccionario inicial de sensores
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}

# Imprime antes de actualizar
print("Before", sensors)

# Agrega múltiples elementos al diccionario
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})

# Imprime después de actualizar
print("After", sensors)


# Diccionario de usuarios con sus IDs
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

# Imprime el diccionario inicial
print(user_ids)

# Actualiza el diccionario con nuevos usuarios
user_ids.update({"theLooper": 138475, "stringQueen": 85739})

# Imprime el diccionario actualizado
print(user_ids)


## Sobrescribir valores

# Ejemplo de agregar o modificar una clave
menu["banana"] = 3

# Diccionario de menú
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

# Imprime antes de modificar
print("Before: ", menu)

# Cambia el valor de una clave existente
menu["oatmeal"] = 5

# Imprime después de modificar
print("After", menu)


# Diccionario con ganadores de los Oscar
oscar_winners = {
    "Best Picture": "La La Land",
    "Best Actor": "Casey Affleck",
    "Best Actress": "Emma Stone",
    "Animated Feature": "Zootopia"
}

# Imprime antes de modificar
print("Before", oscar_winners)
print()

# Agrega una nueva categoría
oscar_winners.update({"Supporting Actress": "Viola Davis"})

# Imprime después de agregar
print("After1", oscar_winners)
print()

# Sobrescribe un valor existente
oscar_winners["Best Picture"] = "Moonlight"

# Imprime después de modificar
print("After2", oscar_winners)


### Comprensión de diccionarios

# Lista de nombres
names = ['Jenny', 'Alexus', 'Sam', 'Grace']

# Lista de alturas
heights = [61, 70, 67, 64]

# Combina ambas listas en pares (tuplas)
zipStudents = zip(names, heights)

# Imprime el objeto zip
print("zipStudents: ", zipStudents)

# Crea un diccionario a partir de las listas usando comprensión
students = {key: value for key, value in zip(names, heights)}

# Imprime el diccionario resultante
print(students)


# Listas de bebidas y contenido de cafeína
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

# Combina las listas
zipped_drinks = zip(drinks, caffeine)

# Imprime el objeto zip
print(zipped_drinks)

# Crea un diccionario con comprensión
drinks_to_caffeine = {key: value for key, value in zipped_drinks}

# Imprime el diccionario
print(drinks_to_caffeine)


# Lista de canciones
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]

# Lista de reproducciones
playcounts = [78, 29, 44, 21, 89, 5]

# Crea un diccionario combinando ambas listas
plays = {key: value for key, value in zip(songs, playcounts)}

# Imprime el diccionario
print(plays)

# Agrega una nueva canción
plays.update({"Purple Haze": 1})

# Modifica el valor de una canción existente
plays.update({"Respect": 94})

# Imprime el diccionario actualizado
print("After: ", plays)

# Diccionario que contiene otros diccionarios
library = {"The Best Songs": plays, "Sunday Feelings": {}}

# Imprime la biblioteca
print(library)