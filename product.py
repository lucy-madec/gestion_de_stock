from database import Database

class Product:
    # Connexion à la base de données
    def __init__(self):
        self.db = Database(host='localhost', user='root', password='', database='zoo')
        