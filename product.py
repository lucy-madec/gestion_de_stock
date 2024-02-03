from database import Database

def get_product_list(category_id=None):
    db = Database("localhost", "root", "&Dance13008", "store")
    query = "SELECT * FROM product WHERE id_category = %s"
    params = (category_id,)
    result = db.fetch_all(query, params)

    # Convertir le résultat en une liste de tuples contenant les informations des produits
    products = [(row[0], row[1], row[2], row[3], row[4]) for row in result]
    return products