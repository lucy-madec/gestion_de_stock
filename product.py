from database import Database

def get_product_list():
    db = Database("localhost", "root", "&Dance13008", "store")

    # Requête pour récupérer la liste de produits
    query = "SELECT * FROM product"
    products = db.fetch_all(query)

    return products