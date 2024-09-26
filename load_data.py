import csv
from pymongo import UpdateOne
from datetime import datetime
from models.director import Director
from models.cast import Cast
from database import Database

# Connexion à la base de donnée
db = Database().connection
collection = db['movies']

# Utilisation de datetime pour obtenir l'année actuelle
current_year = datetime.now().year

# Definition du validateur pour la collection movies
validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["Title", "Year", "IMDB ID", "Runtime", "Rating"],
        "properties": {
            "Title": {
                "bsonType": "string",
                "description": "Doit être une chaîne de caractères et est obligatoire"
            },
            "Year": {
                "bsonType": "int",
                "minimum": 1900,
                "maximum": current_year,
                "description": f"Doit être une date entre 1900 et {current_year} et est obligatoire"
            },
            "IMDB ID": {
                "bsonType": "string",
                "description": "Doit être une chaîne de caractères et est obligatoire"
            },
            "Runtime": {
                "bsonType": "int",
                "description": "Doit être un entier et est obligatoire"
            },
            "Rating": {
                 "bsonType": "double",
                "minimum": 0.1,
                "maximum": 10.0,
                "description": "Doit être un nombre décimal entre 0.1 et 10.0 et est obligatoire"
            },
        }
    }
}

# Creation de la collection avec le validateur si elle n'existe pas
if "movies" not in db.list_collection_names():
    db.create_collection("movies", validator=validator)
else:
    db.command("collMod", "movies", validator=validator)

# Fonction pour lire le fichier CSV
def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield {
                "Title": row["Title"],
                "Year": int(row["Year"]),
                "Summary": row["Summary"],
                "Short Summary": row["Short Summary"],
                "IMDB ID": row["IMDB ID"],
                "Runtime": int(row["Runtime"]),
                "YouTube Trailer": row["YouTube Trailer"],
                "Rating": float(row["Rating"]),
                "Movie Poster": row["Movie Poster"],
                "Director": row["Director"],
                "Writers": row["Writers"],
                "Cast": row["Cast"]
            }

# Lire le fichier CSV et insérer les données dans la collection
def import_data(file_path):
    operations = []

    for movie in read_csv(file_path):
        director_name = movie["Director"]
        director = Director(director_name)
        if not director.exists():
            director.save()

        operations.append(
            UpdateOne(
                {"IMDB ID": movie["IMDB ID"]},
                {"$set": movie},
                upsert=True
            )
        )
        director.add_movie(movie["IMDB ID"])

        # Remplissage du dictionnaire du casting
        cast_list = movie["Cast"].split('|')
        for actor_name in cast_list:
            actor_name = actor_name.strip()
            if actor_name:  # Ensure the cast name is not empty
                actor = Cast(actor_name)
                if not actor.exists():
                    actor.save()
                actor.add_movie(movie["IMDB ID"])

    if operations:
        result = collection.bulk_write(operations)
        print(f"Inséré: {result.upserted_count}, Modifié: {result.modified_count}")

if __name__ == "__main__":
    import_data('ressources/movies.csv')
    print("Base de données crée et données importées.")