from pymongo import MongoClient
from database import Database

#Connexion à la base de données
db = Database().connection

#Creation de la classe Cast
class Cast:
    def __init__(self, actor):
        self.collection = db['cast']
        self.actor = actor

#Fonction pour vérifier si un acteur existe
    def exists(self):
        return self.collection.find_one({"actor": self.actor}) is not None

#Fonction pour créer un nouvel acteur
    def save(self):
        if not self.exists():
            self.collection.insert_one({"actor": self.actor, "movies": []})

#Fonction pour ajouter un film à un acteur
    def add_movie(self, movie_id):
        self.collection.update_one(
            {"actor": self.actor},
            {"$addToSet": {"movies": movie_id}}
        )