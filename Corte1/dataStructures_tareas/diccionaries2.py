#### Get A Key

# Diccionario con alturas de edificios
building_heights = {
    "Burj Khalifa": 828,
    "Shanghai Tower": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Lotte World Tower": 554.5,
    "One World Trade": 541.3
}

# Accede al valor asociado a la clave "Burj Khalifa"
print(building_heights["Burj Khalifa"])  # Imprime 828

# Accede al valor asociado a la clave "Ping An"
print(building_heights["Ping An"])  # Imprime 599


# Diccionario con elementos del zodiaco
zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
}

# Imprime la lista de signos del elemento tierra
print(zodiac_elements["earth"])

# Imprime la lista de signos del elemento fuego
print(zodiac_elements["fire"])


## Get an Invalid Key

# Diccionario nuevamente
building_heights = {
    "Burj Khalifa": 828,
    "Shanghai Tower": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Lotte World Tower": 554.5,
    "One World Trade": 541.3
}

# Intenta acceder a una clave que no existe (esto genera error)
print(building_heights["Landmark 81"])


## Evitar error verificando la clave

# Clave a verificar
key_to_check = "Landmark 81"

# Verifica si la clave existe antes de acceder
if key_to_check in building_heights:
    print(building_heights["Landmark 81"])


# Diccionario de elementos del zodiaco
zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
}

# Agrega una nueva clave con valor
zodiac_elements["energy"] = "Not a Zodiac element"

# Verifica si la clave existe antes de imprimir
if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])


## Safely Get a Key

# Diccionario de edificios
building_heights = {
    "Burj Khalifa": 828,
    "Shanghai Tower": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Lotte World Tower": 554.5,
    "One World Trade": 541.3
}

# Obtiene valor con .get()
building_heights.get("Shanghai Tower")  # Retorna 632

# Intenta obtener una clave inexistente (retorna None)
building_heights.get("My House")


# Diccionario de usuarios
user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}

# Obtiene valor de una clave
user_ids.get("teraCoder")

# Verifica si el valor es None
if user_ids.get("teraCoder") == None:
    tc_id = 1000
else:
    tc_id = user_ids.get("teraCoder")

# Imprime el valor final
print(tc_id)


# Verifica otra clave inexistente
if user_ids.get("superStackSmash") == None:
    stack_id = 100000

# Imprime el valor asignado
print(stack_id)


### Delete a Key

# Diccionario de premios
raffle = {
    223842: "Teddy Bear",
    872921: "Concert Tickets",
    320291: "Gift Basket",
    412123: "Necklace",
    298787: "Pasta Maker"
}

# Elimina una clave existente
print(raffle.pop(320291, "No Prize"))  # Imprime "Gift Basket"

# Imprime el diccionario actualizado
print(raffle)

# Intenta eliminar una clave inexistente
print(raffle.pop(100000, "No Prize"))  # Imprime "No Prize"

# Imprime el diccionario
print(raffle)

# Elimina otra clave existente
print(raffle.pop(872921, "No Prize"))  # Imprime "Concert Tickets"

# Imprime el diccionario final
print(raffle)


# Diccionario de items disponibles
available_items = {
    "health potion": 10,
    "cake of the cure": 5,
    "green elixir": 20,
    "strength sandwich": 25,
    "stamina grains": 15,
    "power stew": 30
}

# Puntos de vida iniciales
health_points = 20

# Suma el valor eliminado (si existe)
health_points += available_items.pop("stamina grains", 0)

# Suma otro valor eliminado
health_points += available_items.pop("power stew", 0)

# Intenta eliminar uno que no existe (suma 0)
health_points += available_items.pop("mystic bread", 0)

# Imprime el diccionario restante
print(available_items)

# Imprime los puntos de vida finales
print(health_points)


## Get All Keys

# Diccionario de notas
test_scores = {
    "Grace": [80, 72, 90],
    "Jeffrey": [88, 68, 81],
    "Sylvia": [80, 82, 84],
    "Pedro": [98, 96, 95],
    "Martin": [78, 80, 78],
    "Dina": [64, 60, 75]
}

# Convierte las claves en lista
print(list(test_scores))

# Recorre e imprime cada clave
for student in test_scores.keys():
    print(student)


# Diccionarios adicionales
user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}

num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18
}

# Obtiene solo las claves
users = user_ids.keys()
lessons = num_exercises.keys()

# Imprime las claves
print(users)
print(lessons)


## Get All Values

# Recorre los valores del diccionario
for score_list in test_scores.values():
    print(score_list)


# Inicializa acumulador
total_exercises = 0

# Suma todos los valores
for exercises in num_exercises.values():
    total_exercises += exercises

# Imprime el total
print(total_exercises)


## Get All Items

# Diccionario de marcas y valores
biggest_brands = {
    "Apple": 184,
    "Google": 141.7,
    "Microsoft": 80,
    "Coca-Cola": 69.7,
    "Amazon": 64.8
}

# Recorre clave y valor simultáneamente
for company, value in biggest_brands.items():
    print(company + " has a value of " + str(value) + " billion dollars.")


# Diccionario de porcentajes
pct_women_in_occupation = {
    "CEO": 28,
    "Engineering Manager": 9,
    "Pharmacist": 58,
    "Physician": 40,
    "Lawyer": 37,
    "Aerospace Engineer": 9
}

# Recorre e imprime información formateada
for occupation, percentage in pct_women_in_occupation.items():
    print("Women make up " + str(percentage) + " percent of " + occupation + "s.")