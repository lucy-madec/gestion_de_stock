import tkinter as tk
from tkinter import ttk

def action(event):
    # Obtenir l'élément sélectionné
    select = listeCombo.get()
    print("Vous avez sélectionné : '", select, "'")

def ajouter_produit():
    # Ajouter une entrée au tableau avec les détails du produit
    produit = listeCombo.get()
    quantite = entryQuantite.get()
    prix = entryPrix.get()

    # Assurez-vous que la quantité et le prix sont des nombres
    try:
        quantite = int(quantite)
        prix = float(prix)
    except ValueError:
        print("La quantité et le prix doivent être des nombres.")
        return

    # Ajouter l'entrée au tableau
    tree.insert("", tk.END, values=(produit, quantite, prix))

# Création de la fenêtre principale
root = tk.Tk() 
root.geometry('800x500')
root.title("Gestion des stocks")

# Widgets pour la sélection de catégorie
labelChoix = tk.Label(root, text="Veuillez choisir une catégorie !")
labelChoix.pack()
labelChoix.place(x=100, y=10)

listeProduits = ["Catégorie 1", "Catégorie 2", "Catégorie 3"]
listeCombo = ttk.Combobox(root, values=listeProduits)
listeCombo.current(0)
listeCombo.place(x=100, y=30)

# Widgets pour le tableau
tree = ttk.Treeview(root, columns=("Article", "Prix", "Quantité"), show="headings")
tree.heading("Article", text="Article")
tree.heading("Prix", text="Prix")
tree.heading("Quantité", text="Quantité")
tree.pack(pady=60)

# Widgets pour l'ajout d'un produit
entryQuantite = tk.Entry(root, width=10)
entryPrix = tk.Entry(root, width=10)

labelQuantite = tk.Label(root, text="Prix:")
labelPrix = tk.Label(root, text="Quantité:")

buttonAjouter = tk.Button(root, text="Ajouter Produit", command=ajouter_produit)

labelQuantite.pack(side=tk.LEFT, padx=5)
entryQuantite.pack(side=tk.LEFT, padx=5)
labelPrix.pack(side=tk.LEFT, padx=5)
entryPrix.pack(side=tk.LEFT, padx=5)
buttonAjouter.pack(side=tk.LEFT, padx=5)

# Lier la fonction action au changement de sélection dans la Combobox
listeCombo.bind("<<ComboboxSelected>>", action)

root.mainloop()