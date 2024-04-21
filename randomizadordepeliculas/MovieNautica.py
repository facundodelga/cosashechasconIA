import random

# Lista de nombres de películas
#movies = ["Forrest Gump", "El padrino", "Titanic", "Origen", "Django Unchained", "La La Land", "El caballero oscuro", "Gladiator", "Shutter Island", "Pulp Fiction"]

# Función que elige una película al azar y la elimina de la lista
def choose_and_remove_movie():
    
    with open("peliculas.txt", "r") as archivo:
        movies = [line.rstrip() for line in archivo]
    print(" ")
    print(" ")
    print(">>>Peliculas de la lista<<<")
    
    if not movies:
        return "No hay más películas en la lista."
    
    for pelicula in movies:
        print(f"    >{pelicula}<")
    print(" ")
    print(" ")
    # Elegir una película al azar
    chosen_movie = random.choice(movies)
    print(f">>  La película elegida al azar es: {chosen_movie}")
    print(" ")
    print(" ")
    # Eliminar la película de la lista
    movies.remove(chosen_movie)
    
    with open("peliculas.txt", "w") as archivo:
        for movie in movies:
            archivo.write(f"{movie}\n")
    
    return f"La lista de películas ahora es: {movies}"

# Llamar a la función
result = choose_and_remove_movie()
print(result)