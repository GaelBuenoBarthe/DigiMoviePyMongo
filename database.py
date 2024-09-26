from pymongo import MongoClient

# Classe Database avec définition de la connexion à la base de données
class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.client = MongoClient('mongodb://localhost:27017/')
            cls._instance.db = cls._instance.client['cinema_gaelBuenoBarthe']
        return cls._instance

    @property
    def connection(self):
        return self.db