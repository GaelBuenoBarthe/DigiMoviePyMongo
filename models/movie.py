from models.base_model import BaseModel
from models.director import Director
from database import Database

#Connexion à la base de données
db = Database().connection

#Creation de la classe Movie
class Movie(BaseModel):
    def __init__(self, imdb_id):
        super().__init__(imdb_id)
        self.imdb_id = imdb_id

#Fonction pour vérifier si un film existe
    def exists(self):
        return db.movies.find_one({"IMDB ID": self.imdb_id}) is not None

#Fonction pour créer un nouveau film
    def save(self, movie_data):
        db.movies.update_one({"IMDB ID": self.imdb_id}, {"$set": movie_data}, upsert=True)

#Fonction pour choisir un directeur existant
    def choose_existing_director(self):
        directors = db.directors.find()
        print("Liste des directeurs existants :")
        for director in directors:
            print(director['name'])
        self.director = input("Choisissez un directeur parmi la liste ci-dessus : ").strip()
        director = Director(self.director)
        if not director.exists():
            print(f"Le directeur '{self.director}' n'existe toujours pas.")
            self.choose_existing_director()

#Fonction pour créer ou modifier un film
    def list_movies(self):
        movies = db.movies.find()
        for movie in movies:
            print(f"Title: {movie['Title']}, Year: {movie['Year']}, IMDB ID: {movie['IMDB ID']}, Runtime: {movie['Runtime']}, Rating: {movie['Rating']}, Director: {movie['Director']}")
            print("\n" + "-"*40 + "\n")

#Fonction pour créer ou modifier un film
    def update_movie(self, imdb_id, **kwargs):
        movie = db.movies.find_one({"IMDB ID": imdb_id})
        if not movie:
            print(f"Le film avec l'ID IMDB '{imdb_id}' n'existe pas.")
            return

        update_data = {}
        for key, value in kwargs.items():
            if value is not None:
                update_data[key] = value

        if 'Director' in update_data:
            director = Director(update_data['Director'])
            if not director.exists():
                print(f"Le directeur '{update_data['Director']}' n'existe pas.")
                self.choose_existing_director()
            director.add_movie(imdb_id)

        db.movies.update_one(
            {"IMDB ID": imdb_id},
            {"$set": update_data}
        )
        print(f"Le film avec l'ID IMDB '{imdb_id}' a été mis à jour.")