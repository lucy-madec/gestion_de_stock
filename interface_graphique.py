import tkinter as tk
from tkinter import ttk, messagebox
from category import get_category_id_by_name
from database import Database
from product import get_product_list

# Fonction pour récupérer et afficher la liste des produits dans le Treeview
def afficher_liste_produits(event=None):
    selected_category = listeCombo.get().strip()

    # Utiliser la fonction get_category_id_by_name pour obtenir l'ID de la catégorie à partir de la base de données
    category_id = get_category_id_by_name(selected_category)

    # Vérifier si l'ID de la catégorie est trouvé
    if category_id is not None:

        # Récupérer les produits de la catégorie correspondante
        products = get_product_list(category_id)

        # Effacer le tableau actuel
        for item in tree.get_children():
            tree.delete(item)

        # Ajouter les produits dans le Treeview
        for product in products:
            tree.insert("", tk.END, values=product)
    else:
        pass

# Création de la fenêtre principale
root = tk.Tk() 
root.geometry('1000x500')
root.title("Gestion des stocks - IGolf")

def action(event):
    # Obtenir l'élément sélectionné
    select = listeCombo.get()
    print("Vous avez sélectionné : '", select, "'")

def ajouter_produit():
    # Récupérer le nom du produit , la quantité, le prix et la description entrés par l'utilisateur
    id = entryId.get()
    produit = entryProduit.get()
    description = entryDescription.get()
    quantite = entryQuantite.get()
    prix = entryPrix.get()

    # Quantité et prix
    try:
        id = int(id)
        quantite = int(quantite)
        prix = int(prix)
    except ValueError:
        print("La quantité et le prix doivent être des nombres.")
        return

    # Ajouter l'entrée au tableau
    tree.insert("", tk.END, values=(id, produit, description, quantite, prix))

# Widgets pour la sélection de catégorie
labelChoix = tk.Label(root, text="Veuillez choisir une catégorie")
labelChoix.pack()
labelChoix.place(x=95, y=5)

listeProduits = ["Clubs", "Accessoires", "Vêtements"]
listeCombo = ttk.Combobox(root, values=listeProduits)
listeCombo.current(0)
listeCombo.place(x=100, y=30)

# Widgets pour le tableau
tree = ttk.Treeview(root, columns=("Id","Produit", "Description", "Prix", "Quantité"), show="headings")
tree.heading("Id", text="Id")
tree.heading("Produit", text="Produit")
tree.heading("Description", text="Description")
tree.heading("Prix", text="Prix")
tree.heading("Quantité", text="Quantité")
tree.grid(row=0, column=0, sticky='nsew', padx=50, pady=50)
tree.pack(pady=70, padx=50)

# Ajuster la largeur des colonnes
tree.column("Id", width=40, anchor=tk.CENTER)
tree.column("Produit", width=260, anchor=tk.CENTER)
tree.column("Description", width=150, anchor=tk.CENTER)
tree.column("Prix", width=80, anchor=tk.CENTER)
tree.column("Quantité", width=80, anchor=tk.CENTER)

# Appeler la fonction pour afficher la liste des produits au démarrage de l'interface
afficher_liste_produits()

# Créer la frame pour les boutons "Modifier produit" et "Supprimer produit"
frame_boutons = tk.Frame(root)
frame_boutons.pack(side=tk.RIGHT, padx=10)

# Widgets pour l'ajout d'un produit
entryId = tk.Entry(root, width=5)
entryProduit = tk.Entry(root, width=20)
entryDescription = tk.Entry(root, width=20)
entryQuantite = tk.Entry(root, width=10)
entryPrix = tk.Entry(root, width=10)

labelId = tk.Label(root, text="Id:")
labelProduit = tk.Label(root, text="Produit:")
labelDescription = tk.Label(root, text="Description:")
labelQuantite = tk.Label(root, text="Prix:")
labelPrix = tk.Label(root, text="Quantité:")

buttonAjouter = tk.Button(root, text="Ajouter produit", command=ajouter_produit)

labelId.pack(side=tk.LEFT, padx=5)
entryId.pack(side=tk.LEFT, padx=5)
labelProduit.pack(side=tk.LEFT, padx=5)
entryProduit.pack(side=tk.LEFT, padx=5)
labelDescription.pack(side=tk.LEFT, padx=5)
entryDescription.pack(side=tk.LEFT, padx=5)
labelQuantite.pack(side=tk.LEFT, padx=5)
entryQuantite.pack(side=tk.LEFT, padx=5)
labelPrix.pack(side=tk.LEFT, padx=5)
entryPrix.pack(side=tk.LEFT, padx=5)
buttonAjouter.pack(side=tk.LEFT, padx=5)

# Fonction pour gérer la sélection d'un produit dans le Treeview
def on_product_select(event):
    global selected_product_id
    selected_product_id = tree.focus() # Stocker l'ID du produit sélectionné
    item = tree.item(selected_product_id)
    values = item['values']
    entryId.delete(0, tk.END)
    entryId.insert(0, values[0])
    entryProduit.delete(0, tk.END)
    entryProduit.insert(0, values[1])
    entryDescription.delete(0, tk.END)
    entryDescription.insert(0, values[2])
    entryPrix.delete(0, tk.END)
    entryPrix.insert(0, values[3])
    entryQuantite.delete(0, tk.END)
    entryQuantite.insert(0, values[4])
    buttonModifier.config(state=tk.NORMAL) # Activer le bouton Modifier

# Fonction pour gérer la modification d'un produit
def modifier_produit():
    id = entryId.get()
    produit = entryProduit.get()
    description = entryDescription.get()
    prix = entryPrix.get()
    quantite = entryQuantite.get()

    # Afficher une boîte de dialogue de confirmation
    if messagebox.askyesno('Confirmation', 'Êtes-vous sûr de vouloir modifier ce produit ?'):
        # Mettre à jour les détails du produit dans la base de données
        db = Database("localhost", "root", "&Dance13008", "store")
        query = "UPDATE product SET name = %s, description = %s, price = %s, quantity = %s WHERE id = %s"
        params = (produit, description, prix, quantite, id)
        db.query(query, params)
        db.connexion.close()

        # Mettre à jour les détails du produit dans le Treeview
        tree.item(selected_product_id, values=(id, produit, description, prix, quantite))
        buttonModifier.config(state=tk.DISABLED) # Désactiver le bouton Modifier
        buttonMettreAJour.destroy() # Supprimer le bouton Mettre à jour
    else:
        # Annuler les modifications
        buttonMettreAJour.destroy() # Supprimer le bouton Mettre à jour

# Créer le bouton de modification
buttonModifier = tk.Button(root, text="Modifier produit", command=modifier_produit, state=tk.DISABLED)
buttonModifier.place(x=850, y=70)

# Créer le bouton Mettre à jour qui sera affiché après la modification
buttonMettreAJour = tk.Button(root, text="Mettre à jour", command=modifier_produit, state=tk.DISABLED)
buttonMettreAJour.place(x=850, y=110)

# Créer le bouton Mettre à jour qui sera affiché après la modification
buttonMettreAJour = tk.Button(root, text="Mettre à jour", command=modifier_produit, state=tk.DISABLED)

def supprimer_produit():
    # Obtenir l'identifiant de l'élément sélectionné
    selection = tree.selection()
    if selection:
        # Supprimer l'élément sélectionné
        tree.delete(selection)
    else:
        print("Aucun produit a été sélectionné pour être supprimé.")

# Créer le bouton de suppression
buttonSupprimer = tk.Button(root, text="Supprimer produit", command=supprimer_produit, state=tk.DISABLED)

# Empaqueter le bouton de suppression
buttonSupprimer.place(x=850, y=110)

# Fonction pour gérer la visibilité du bouton de suppression
def on_tree_select(event):
    # Vérifier si un élément est sélectionné
    selection = tree.selection()
    if selection:
        # Activer le bouton si un élément est sélectionné
        buttonSupprimer.config(state=tk.NORMAL)
    else:
        # Désactiver le bouton si aucun élément n'est sélectionné
        buttonSupprimer.config(state=tk.DISABLED)

# Lier la fonction on_tree_select à l'événement de sélection du tableau
tree.bind("<FocusIn>", on_tree_select)

# Lier la fonction on_product_select à l'événement de sélection du tableau
tree.bind("<Double-1>", on_product_select)

# Lier la fonction afficher_liste_produits à l'événement de sélection de la Combobox
listeCombo.bind("<<ComboboxSelected>>", afficher_liste_produits)

root.mainloop()