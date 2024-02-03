import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.connexion = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        self.cursor = self.connexion.cursor()
    
    # Demander une requête à la base de données
    def query(self, query, params= None):
        self.cursor.execute(query, params or ())
        self.connexion.commit()

    # Prendre les données de la base de données
    def fetch_all(self, query, params= None):
        self.cursor.execute(query, params if params is not None else ())
        return self.cursor.fetchall()
    