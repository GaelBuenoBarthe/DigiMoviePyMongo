from database import Database

# Connexion à la base de données
db = Database().connection

# Fonction pour obtenir les 15 acteurs ayant tourné dans le plus de films
def top_actors_by_movie_count():
    pipeline = [
        {"$unwind": "$movies"},
        {"$lookup": {
            "from": "movies",
            "localField": "movies",
            "foreignField": "IMDB ID",
            "as": "movie_details"
        }},
        {"$unwind": "$movie_details"},
        {"$lookup": {
            "from": "directors",
            "localField": "movie_details.Director",
            "foreignField": "name",
            "as": "director_details"
        }},
        {"$unwind": "$director_details"},
        {"$group": {
            "_id": "$actor",
            "movieCount": {"$sum": 1},
            "movies": {"$push": {
                "title": "$movie_details.Title",
                "year": "$movie_details.Year",
                "director": "$director_details.name"
            }}
        }},
        {"$sort": {"movieCount": -1}},
        {"$limit": 15},
        {"$project": {
            "actor": "$_id",
            "movieCount": 1,
            "movies": {
                "$map": {
                    "input": "$movies",
                    "as": "movie",
                    "in": {
                        "$concat": [
                            "$$movie.title",
                            " (",
                            {"$toString": "$$movie.year"},
                            " réalisé par ",
                            {"$cond": {
                                "if": {"$eq": ["$$movie.director", "$_id"]},
                                "then": "lui-même",
                                "else": "$$movie.director"
                            }},
                            ")"
                        ]
                    }
                }
            },
            "_id": 0
        }}
    ]
    return list(db.cast.aggregate(pipeline))