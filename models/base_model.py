from database import Database

#Connexion à la base de données
db = Database().connection

#Creation de la classe BaseModel
class BaseModel:
    def __init__(self, _id):
        self._id = _id

    @classmethod
    def get_by_id(cls, _id):
        return db[cls.__name__.lower() + 's'].find_one({"_id": _id})