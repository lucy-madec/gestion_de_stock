import tkinter as tk
from tkinter import ttk

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
    produit = entryProduit.get()
    description = entryDescription.get()
    quantite = entryQuantite.get()
    prix = entryPrix.get()

    # Quantité et prix
    try:
        quantite = int(quantite)
        prix = int(prix)
    except ValueError:
        print("La quantité et le prix doivent être des nombres.")
        return

    # Ajouter l'entrée au tableau
    tree.insert("", tk.END, values=(produit, description, quantite, prix))

# Widgets pour la sélection de catégorie
labelChoix = tk.Label(root, text="Veuillez choisir une catégorie")
labelChoix.pack()
labelChoix.place(x=95, y=5)

listeProduits = ["Clubs", "Accessoires", "Vêtements"]
listeCombo = ttk.Combobox(root, values=listeProduits)
listeCombo.current(0)
listeCombo.place(x=100, y=30)

# Widgets pour le tableau
tree = ttk.Treeview(root, columns=("Article", "Description", "Prix", "Quantité"), show="headings")
tree.heading("Article", text="Article")
tree.heading("Description", text="Description")
tree.heading("Prix", text="Prix")
tree.heading("Quantité", text="Quantité")
tree.grid(row=0, column=0, sticky='nsew', padx=50, pady=50)
tree.pack(pady=70, padx=50)


# Widgets pour l'ajout d'un produit
entryProduit = tk.Entry(root, width=20)
entryDescription = tk.Entry(root, width=20)
entryQuantite = tk.Entry(root, width=10)
entryPrix = tk.Entry(root, width=10)

labelProduit = tk.Label(root, text="Article:")
labelDescription = tk.Label(root, text="Description:")
labelQuantite = tk.Label(root, text="Prix:")
labelPrix = tk.Label(root, text="Quantité:")

buttonAjouter = tk.Button(root, text="Ajouter Produit", command=ajouter_produit)

labelProduit.pack(side=tk.LEFT, padx=5)
entryProduit.pack(side=tk.LEFT, padx=5)
labelDescription.pack(side=tk.LEFT, padx=5)
entryDescription.pack(side=tk.LEFT, padx=5)
labelQuantite.pack(side=tk.LEFT, padx=5)
entryQuantite.pack(side=tk.LEFT, padx=5)
labelPrix.pack(side=tk.LEFT, padx=5)
entryPrix.pack(side=tk.LEFT, padx=5)
buttonAjouter.pack(side=tk.LEFT, padx=5)

# Fonction pour gérer la modification d'un article
def modifier_article():
    # Code pour modifier l'article sélectionné
    pass

# Créer le bouton de modification
buttonModifier = tk.Button(root, text="Modifier Article", command=modifier_article)

# Empaqueter le bouton de modification
buttonModifier.pack(side=tk.LEFT, padx=5)

def supprimer_article():
    # Obtenir l'identifiant de l'élément sélectionné
    selection = tree.selection()
    if selection:
        # Supprimer l'élément sélectionné
        tree.delete(selection)
    else:
        print("Aucun article sélectionné pour supprimer.")

# Créer le bouton de suppression
buttonSupprimer = tk.Button(root, text="Supprimer Article", command=supprimer_article, state=tk.DISABLED)

# Empaqueter le bouton de suppression
buttonSupprimer.pack(side=tk.LEFT, padx=5)

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

# Lier la fonction action au changement de sélection dans la Combobox
listeCombo.bind("<<ComboboxSelected>>", action)

root.mainloop()