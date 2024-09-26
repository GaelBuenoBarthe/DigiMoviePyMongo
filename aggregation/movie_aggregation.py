from database import Database

# Connexion à la base de donnée
db = Database().connection

# Fonction pour obtenir les 5 films les mieux notés
def top_rated_movies():
    pipeline = [
        {"$match": {"Rating": {"$exists": True}}},  # Ensure Rating field exists
        {"$sort": {"Rating": -1}},
        {"$limit": 5},
        {"$project": {
            "Titre": "$Title",
            "Année": "$Year",
            "Rating": 1,
            "_id": 0
        }}
    ]
    return list(db.movies.aggregate(pipeline))