from models.base_model import BaseModel
from database import Database

#Connexion à la base de données
db = Database().connection

#Creation de la classe Director
class Director(BaseModel):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

#Fonction pour vérifier si un directeur existe
    def exists(self):
        return db.directors.find_one({"name": self.name}) is not None

#Fonction pour créer un nouveau directeur
    def save(self):
        if not self.exists():
            db.directors.insert_one({"name": self.name, "movies": []})

#Fonction pour ajouter un film à un directeur
    def add_movie(self, movie_id):
        db.directors.update_one(
            {"name": self.name},
            {"$addToSet": {"movies": movie_id}}
        )

#Fonction pour lister les films d'un directeur
    def list_movies(self):
        director = db.directors.find_one({"name": self.name})
        return director.get("movies", []) if director else []

#Fonction pour obtenir la note moyenne des films d'un directeur
    def average_rating(self):
        director = db.directors.find_one({"name": self.name})
        if director and director.get("movies"):
            pipeline = [
                {"$match": {"_id": {"$in": director["movies"]}}},
                {"$group": {"_id": None, "averageRating": {"$avg": "$Rating"}}}
            ]
            result = list(db.movies.aggregate(pipeline))
            return result[0]["averageRating"] if result else None
        return None