from aggregation.movie_aggregation import top_rated_movies
from aggregation.director_aggregation import top_rated_directors, top_runtime_directors, most_movies_directors
from aggregation.cast_aggregation import top_actors_by_movie_count, top_actors_by_movie_count_light
from models.director import Director
from database import Database

db = Database().connection

# Fonction pour afficher les résultats
def display_results(results, result_type):
    if not results:
        print(f"Aucun {result_type} trouvé.")
    else:
        for result in results:
            for key, value in result.items():
                print(f"{key}: {value}")
            print("\n" + "-"*40 + "\n")

# Fonction du menu principal
def main_menu():
    while True:
        print("Digi Movie\nMenu Principal:")
        print("1. Agrégations des films")
        print("2. Agrégations des réalisateurs")
        print("3. Créer ou modifier un film")
        print("4. Créer ou modifier un réalisateur")
        print("5. Agrégations des acteurs")
        print("Tapez 'exit' pour quitter.")
        choice = input("Choisissez une option: ").strip().lower()

        if choice == '1':
            movie_aggregation_menu()
        elif choice == '2':
            director_aggregation_menu()
        elif choice == '3':
            create_or_modify_movie()
        elif choice == '4':
            create_or_modify_director()
        elif choice == '5':
            actor_aggregation_menu()
        elif choice == 'exit':
            break
        else:
            print("Option invalide. Veuillez réessayer.")

# Fonction pour afficher les films les mieux notés
def display_top_rated_movies(results):
    if not results:
        print("Aucun film trouvé.")
    else:
        print("Top 5 des films les mieux notés :")
        for index, result in enumerate(results, start=1):
            print(f"{index}. {result['Titre']} ({result['Année']}) - Note : {result['Rating']}")
        print("\n" + "-"*40 + "\n")

# Fonction du menu d'agrégation des films
def movie_aggregation_menu():
    while True:
        print("Menu Agrégations des Films:")
        print("1. Top 5 des films les mieux notés")
        print("Tapez 'exit' pour revenir au menu principal.")
        choice = input("Choisissez une option: ").strip().lower()

        if choice == '1':
            results = top_rated_movies()
            display_top_rated_movies(results)
        elif choice == 'exit':
            break
        else:
            print("Option invalide. Veuillez réessayer.")

# Fonction pour afficher les réalisateurs les mieux notés
def display_top_rated_directors(results):
    if not results:
        print("Aucun réalisateur trouvé.")
    else:
        print("Top 5 des réalisateurs les mieux notés :")
        for index, result in enumerate(results, start=1):
            print(f"{index}. {result['Nom']} - Note moyenne : {result['Note moyenne']} "
                  f"(moyenne calculée sur {result['Nombre de films']} films)")
        print("\n" + "-"*40 + "\n")

# Fonction pour afficher les réalisateurs par durée moyenne des films
def display_top_runtime_directors(results):
    if not results:
        print("Aucun réalisateur trouvé.")
    else:
        print("Top 5 des réalisateurs par durée moyenne des films :")
        for index, result in enumerate(results, start=1):
            print(f"{index}. {result['name']} - Durée moyenne : {result['averageRuntime']} minutes "
                  f"(calculée sur {result['movieCount']} films)")
        print( "-"*40 + "\n")

# Fonction pour afficher les réalisateurs par nombre de films
def display_most_movies_directors(results):
    if not results:
        print("Aucun réalisateur trouvé.")
    else:
        print("Top 5 des réalisateurs par nombre de films :")
        for index, result in enumerate(results, start=1):
            print(f"{index}. {result['Nom']} - Nombre de films : {result['Nombre de films']}")
            print("Films:")
            for movie in result['Movies']:
                print(f" - {movie['Title']} ({movie['Year']})")
            print("\n")

# Fonction du menu d'agrégation des réalisateurs
def director_aggregation_menu():
    while True:
        print("Menu Agrégations des Réalisateurs:")
        print("1. Top 5 des réalisateurs les mieux notés")
        print("2. Top 5 des réalisateurs par durée moyenne des films")
        print("3. Top 5 des réalisateurs par nombre de films")
        print("Tapez 'exit' pour revenir au menu principal.")
        choice = input("Choisissez une option: ").strip().lower()

        if choice == '1':
            results = top_rated_directors()
            display_top_rated_directors(results)
        elif choice == '2':
            results = top_runtime_directors()
            display_top_runtime_directors(results)
        elif choice == '3':
            results = most_movies_directors()
            display_most_movies_directors(results)
        elif choice == 'exit':
            break
        else:
            print("Option invalide. Veuillez réessayer.")

# Fonction pour créer ou modifier un film
def create_or_modify_movie():
    print("Créer ou Modifier un Film:")
    imdb_id = input("Entrez l'IMDB ID du film: ").strip()
    existing_movie = db.movies.find_one({"IMDB ID": imdb_id})

    if existing_movie:
        print("Le film existe déjà. Mise à jour des informations.")
    else:
        print("Création d'un nouveau film.")
        existing_movie = {}

    title = input(f"Entrez le titre du film [{existing_movie.get('Title', '')}]: ").strip() or existing_movie.get('Title', '')
    year = input(f"Entrez l'année de sortie du film [{existing_movie.get('Year', '')}]: ").strip()
    year = int(year) if year else existing_movie.get('Year', '')
    summary = input(f"Entrez le résumé du film [{existing_movie.get('Summary', '')}]: ").strip() or existing_movie.get('Summary', '')
    short_summary = input(f"Entrez le court résumé du film [{existing_movie.get('Short Summary', '')}]: ").strip() or existing_movie.get('Short Summary', '')
    runtime = input(f"Entrez la durée du film (en minutes) [{existing_movie.get('Runtime', '')}]: ").strip()
    runtime = int(runtime) if runtime else existing_movie.get('Runtime', '')
    youtube_trailer = input(f"Entrez le lien de la bande-annonce YouTube [{existing_movie.get('YouTube Trailer', '')}]: ").strip() or existing_movie.get('YouTube Trailer', '')
    rating = input(f"Entrez la note du film [{existing_movie.get('Rating', '')}]: ").strip()
    rating = float(rating) if rating else existing_movie.get('Rating', '')
    movie_poster = input(f"Entrez le lien de l'affiche du film [{existing_movie.get('Movie Poster', '')}]: ").strip() or existing_movie.get('Movie Poster', '')

    while True:
        director_name = input(f"Entrez le nom du réalisateur [{existing_movie.get('Director', '')}]: ").strip() or existing_movie.get('Director', '')
        director = Director(director_name)
        if director.exists():
            break
        else:
            print("Réalisateur introuvable. Veuillez saisir un nom de réalisateur valide.")

    writers = input(f"Entrez les scénaristes du film [{existing_movie.get('Writers', '')}]: ").strip() or existing_movie.get('Writers', '')
    cast = input(f"Entrez le casting du film [{existing_movie.get('Cast', '')}]: ").strip() or existing_movie.get('Cast', '')

    movie = {
        "Title": title,
        "Year": year,
        "Summary": summary,
        "Short Summary": short_summary,
        "IMDB ID": imdb_id,
        "Runtime": runtime,
        "YouTube Trailer": youtube_trailer,
        "Rating": rating,
        "Movie Poster": movie_poster,
        "Director": director_name,
        "Writers": writers,
        "Cast": cast
    }

    db.movies.update_one({"IMDB ID": imdb_id}, {"$set": movie}, upsert=True)
    director.add_movie(imdb_id)
    print("Film créé ou modifié avec succès.")

# Fonction pour créer ou modifier un réalisateur
def create_or_modify_director():
    print("Créer ou Modifier un Réalisateur:")
    name = input("Entrez le nom du réalisateur: ").strip()
    existing_director = db.directors.find_one({"name": name})

    if existing_director:
        print("Le réalisateur existe déjà. Mise à jour des informations.")
    else:
        print("Création d'un nouveau réalisateur.")
        existing_director = {"name": name, "movies": []}

    movie_id = input("Entrez l'IMDB ID du film à ajouter (ou laissez vide pour ne rien ajouter): ").strip()
    if movie_id:
        existing_movie = db.movies.find_one({"IMDB ID": movie_id})
        if not existing_movie:
            print("Film introuvable. Veuillez choisir un film existant.")
            existing_movies = db.movies.find({}, {"_id": 0, "Title": 1, "IMDB ID": 1})
            print("Liste des films existants:")
            for m in existing_movies:
                print(f"- {m['Title']} (IMDB ID: {m['IMDB ID']})")
            return
        if movie_id not in existing_director["movies"]:
            existing_director["movies"].append(movie_id)

    db.directors.update_one({"name": name}, {"$set": existing_director}, upsert=True)
    print("Réalisateur créé ou modifié avec succès.")

# Fonction pour afficher les acteurs les plus présents dans des films
def display_top_actors(results):
    if not results:
        print("Aucun acteur trouvé.")
    else:
        print("Top 15 des acteurs les plus présents dans des films :")
        for index, result in enumerate(results, start=1):
            print(f"{index}. {result['actor']} - Nombre de films : {result['movieCount']}")
            print("Films:")
            for movie in result['movies']:
                print(f" - {movie}")
            print("\n")

# Fonction pour afficher les acteurs les plus présents dans des films (version légère)
def display_top_actors_light(results):
    if not results:
        print("Aucun acteur trouvé.")
    else:
        print("Top 15 des acteurs les plus présents dans des films :")
        for index, result in enumerate(results, start=1):
            print(f"{index}. {result['actor']}")
            print("Films:")
            for movie in result['movies']:
                print(f" - {movie}")
            print("\n")

# Fonction du menu d'agrégation des acteurs
def actor_aggregation_menu():
    while True:
        print("Menu Agrégations des Acteurs:")
        print("1. Top 15 des acteurs les plus présents dans les films")
        print("2. Top 15 des acteurs les plus présents dans les films (version légère)")
        print("Tapez 'exit' pour revenir au menu principal.")
        choice = input("Choisissez une option: ").strip().lower()

        if choice == '1':
            results = top_actors_by_movie_count()
            display_top_actors(results)
        elif choice == '2':
            results = top_actors_by_movie_count_light()
            display_top_actors_light(results)
        elif choice == 'exit':
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main_menu()