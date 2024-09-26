from database import Database

# Connexion à la base de donnée
db = Database().connection

# Fonction pour obtenir les 5 réalisateurs les mieux notés
def top_rated_directors():
    pipeline = [
        {"$unwind": "$movies"},
        {"$lookup": {
            "from": "movies",
            "localField": "movies",
            "foreignField": "IMDB ID",
            "as": "movie_details"
        }},
        {"$unwind": "$movie_details"},
        {"$group": {
            "_id": "$name",
            "averageRating": {"$avg": "$movie_details.Rating"},
            "movieCount": {"$sum": 1}
        }},
        {"$sort": {"averageRating": -1}},
        {"$limit": 5},
        {"$project": {
            "Nom": "$_id",
            "Note moyenne": "$averageRating",
            "Nombre de films": "$movieCount",
            "_id": 0
        }}
    ]
    return list(db.directors.aggregate(pipeline))

# Fonction pour obtenir les 5 réalisateurs par durée moyenne des films
def top_runtime_directors():
    pipeline = [
        {"$unwind": "$movies"},
        {"$lookup": {
            "from": "movies",
            "localField": "movies",
            "foreignField": "IMDB ID",
            "as": "movie_details"
        }},
        {"$unwind": "$movie_details"},
        {"$group": {
            "_id": "$name",
            "averageRuntime": {"$avg": "$movie_details.Runtime"},
            "movieCount": {"$sum": 1}
        }},
        {"$project": {
            "name": "$_id",
            "averageRuntime": {"$ceil": "$averageRuntime"},
            "movieCount": 1
        }},
        {"$sort": {"averageRuntime": -1}},
        {"$limit": 5}
    ]
    return list(db.directors.aggregate(pipeline))

# Fonction pour obtenir les 5 réalisateurs par nombre de films
def most_movies_directors():
    pipeline = [
        {"$lookup": {
            "from": "movies",
            "localField": "movies",
            "foreignField": "IMDB ID",
            "as": "movie_details"
        }},
        {"$project": {
            "Nom": "$name",
            "Nombre de films": {"$size": "$movies"},
            "Movies": {
                "$map": {
                    "input": "$movie_details",
                    "as": "movie",
                    "in": {"Title": "$$movie.Title", "Year": "$$movie.Year"}
                }
            }
        }},
        {"$sort": {"Nombre de films": -1}},
        {"$limit": 5},
        {"$project": {
            "Nom": 1,
            "Nombre de films": 1,
            "Movies": 1,
            "_id": 0
        }}
    ]
    return list(db.directors.aggregate(pipeline))