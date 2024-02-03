from database import Database

def get_category_id_by_name(category_name):
    db = Database("localhost", "root", "", "store")
    query = "SELECT id FROM category WHERE name = %s"
    params = (category_name,)
    result = db.fetch_all(query, params)

    if result:
        # Si une catégorie correspondante est trouvée, retourne son ID
        return result[0][0]
    else:
        # Si aucune catégorie n'est trouvée, retourne None ou une valeur par défaut
        return None