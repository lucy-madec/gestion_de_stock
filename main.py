import tkinter as tk
from tkinter import ttk, messagebox
from category import get_category_id_by_name
from database import Database
from product import get_product_list

# Fonction pour récupérer et afficher la liste des produits dans le Treeview (Tableau)
def display_list_products(event=None):
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

def add_product():
    # Récupérer le nom du produit , la quantité, le prix et la description entrés par l'utilisateur
    product = entryProduct.get()
    description = entryDescription.get()
    quantity = entryQuantity.get()
    price = entryPrice.get()

    # Vérifier si les champs requis ne sont pas vides
    if not product or not description or not quantity or not price:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        return

    # Quantité et prix
    try:
        quantity = int(quantity)
        price = int(price)
    except ValueError:
        messagebox.showerror("Erreur", "La quantité et le prix doivent être des nombres.")
        return
    
    # Insérer le produit dans la base de données
    db = Database("localhost", "root", "", "store")
    query = "INSERT INTO product (name, description, price, quantity) VALUES (%s, %s, %s, %s)"
    params = (product, description, price, quantity)
    cursor = db.connexion.cursor()
    cursor.execute(query, params)
    db.connexion.commit()
    product_id = cursor.lastrowid # Récupérer l'ID généré

    # Ajouter l'entrée au tableau
    tree.insert("", tk.END, values=(product_id, product, description, quantity, price))

    # Fermer la connexion à la base de données
    db.connexion.close()

    # Effacer les champs d'entrée après l'ajout
    entryProduct.delete(0, tk.END)
    entryDescription.delete(0, tk.END)
    entryQuantity.delete(0, tk.END)
    entryPrice.delete(0, tk.END)

    # Afficher un message de succès
    messagebox.showinfo("Succès", "Produit ajouté avec succès à la base de données.")

# Widgets pour la sélection de catégorie
labelChoice = tk.Label(root, text="Veuillez choisir une catégorie")
labelChoice.pack()
labelChoice.place(x=95, y=5)

listeProducts = ["Clubs", "Accessoires", "Vêtements"]
listeCombo = ttk.Combobox(root, values=listeProducts)
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
display_list_products()

# Créer la frame pour les boutons "Modifier produit" et "Supprimer produit"
frame_boutons = tk.Frame(root)
frame_boutons.pack(side=tk.RIGHT, padx=10)

# Widgets pour l'ajout d'un produit
entryProduct = tk.Entry(root, width=20)
entryDescription = tk.Entry(root, width=20)
entryQuantity = tk.Entry(root, width=10)
entryPrice = tk.Entry(root, width=10)

labelProduct = tk.Label(root, text="Produit:")
labelDescription = tk.Label(root, text="Description:")
labelQuantity = tk.Label(root, text="Prix:")
labelPrice = tk.Label(root, text="Quantité:")

buttonAdd = tk.Button(root, text="Ajouter Product", command=add_product)

labelProduct.pack(side=tk.LEFT, padx=5)
entryProduct.pack(side=tk.LEFT, padx=5)
labelDescription.pack(side=tk.LEFT, padx=5)
entryDescription.pack(side=tk.LEFT, padx=5)
labelQuantity.pack(side=tk.LEFT, padx=5)
entryQuantity.pack(side=tk.LEFT, padx=5)
labelPrice.pack(side=tk.LEFT, padx=5)
entryPrice.pack(side=tk.LEFT, padx=5)
buttonAdd.pack(side=tk.LEFT, padx=5)

# Fonction pour gérer la sélection d'un produit dans le Treeview
def on_product_select(event):
    global selected_product_id
    selected_product_id = tree.focus() # Stocker l'ID du produit sélectionné
    item = tree.item(selected_product_id)
    values = item['values']
    entryProduct.delete(0, tk.END)
    entryProduct.insert(0, values[1])
    entryDescription.delete(0, tk.END)
    entryDescription.insert(0, values[2])
    entryPrice.delete(0, tk.END)
    entryPrice.insert(0, values[3])
    entryQuantity.delete(0, tk.END)
    entryQuantity.insert(0, values[4])
    buttonSet.config(state=tk.NORMAL) # Activer le bouton Modifier

# Fonction pour gérer la modification d'un produit
def set_product():
    product = entryProduct.get()
    description = entryDescription.get()
    price = entryPrice.get()
    quantity = entryQuantity.get()

    # Afficher une boîte de dialogue de confirmation
    if messagebox.askyesno('Confirmation', 'Êtes-vous sûr de vouloir modifier ce produit ?'):
        # Mettre à jour les détails du produit dans la base de données
        db = Database("localhost", "root", "", "store")
        query = "UPDATE product SET name = %s, description = %s, price = %s, quantity = %s WHERE id = %s"
        params = (product, description, price, quantity, id)
        db.query(query, params)
        db.connexion.close()

        # Mettre à jour les détails du produit dans le Treeview
        tree.item(selected_product_id, values=(id, product, description, price, quantity))
        buttonSet.config(state=tk.DISABLED) # Désactiver le bouton Modifier
        buttonUpdate.destroy() # Supprimer le bouton Mettre à jour
    else:
        # Annuler les modifications
        buttonUpdate.destroy() # Supprimer le bouton Mettre à jour

# Créer le bouton de modification
buttonSet = tk.Button(root, text="Modifier produit", command=set_product, state=tk.DISABLED)
buttonSet.place(x=850, y=70)

# Créer le bouton Mettre à jour qui sera affiché après la modification
buttonUpdate = tk.Button(root, text="Mettre à jour", command=set_product, state=tk.DISABLED)
buttonUpdate.place(x=850, y=110)

# Créer le bouton Mettre à jour qui sera affiché après la modification
buttonUpdate = tk.Button(root, text="Mettre à jour", command=set_product, state=tk.DISABLED)

def delete_product():
    # Obtenir l'identifiant de l'élément sélectionné
    select = tree.select()
    if select:
        # Afficher une boîte de dialogue de confirmation
        if messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer ce produit ?"):
            # Supprimer l'élément sélectionné
            tree.delete(select)
            # Afficher un message de succès
            messagebox.showinfo("Succès", "Produit supprimé avec succès.")
    else:
        print("Aucun produit a été sélectionné pour être supprimé.")

# Créer le bouton de suppression
buttonDelete = tk.Button(root, text="Supprimer produit", command=delete_product, state=tk.DISABLED)

# Empaqueter le bouton de suppression
buttonDelete.place(x=850, y=110)

# Fonction pour gérer la visibilité du bouton de suppression
def on_tree_select(event):
    # Vérifier si un élément est sélectionné
    select = tree.select()
    if select:
        # Activer le bouton si un élément est sélectionné
        buttonDelete.config(state=tk.NORMAL)
    else:
        # Désactiver le bouton si aucun élément n'est sélectionné
        buttonDelete.config(state=tk.DISABLED)

# Lier la fonction on_tree_select à l'événement de sélection du tableau
tree.bind("<FocusIn>", on_tree_select)

# Lier la fonction on_product_select à l'événement de sélection du tableau
tree.bind("<Double-1>", on_product_select)

# Lier la fonction afficher_liste_produits à l'événement de sélection de la Combobox
listeCombo.bind("<<ComboboxSelected>>", display_list_products)

root.mainloop()