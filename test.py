import tkinter as tk
from tkinter import ttk
import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="store"
)

cursor = conn.cursor()

# Requête pour récupérer la liste de produits
query = "SELECT * FROM product"
cursor.execute(query)
products = cursor.fetchall()

conn.close()

# Fonction pour afficher les détails du produit sélectionné
def show_product_details():
    selected_item = tree.selection()[0]
    product_details = tree.item(selected_item, 'values')
    print("Détails du produit sélectionné :", product_details)

# Création de l'interface graphique
root = tk.Tk()
root.title("Liste des produits")

# Création du Treeview pour afficher la liste des produits
columns = ('ID', 'Nom', 'Description', 'Prix', 'Quantité', 'ID Catégorie')
tree = ttk.Treeview(root, columns=columns, show='headings')

# Ajout des en-têtes de colonnes
for col in columns:
    tree.heading(col, text=col)

# Ajout des données dans le Treeview
for product in products:
    tree.insert("", "end", values=product)

# Ajout du Treeview à la fenêtre
tree.pack(pady=20)

# Bouton pour afficher les détails du produit sélectionné
details_button = tk.Button(root, text="Afficher les détails", command=show_product_details)
details_button.pack()

root.mainloop()
