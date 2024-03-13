import tkinter as tk

# Créer une fenêtre
window = tk.Tk()

# Créer un bouton
button = tk.Button(window, text="Réinitialiser", command=lambda: reset_graph())

# Ajouter le bouton à la fenêtre
button.pack()

# Démarrer la boucle principale de l'interface graphique
window.mainloop()



def reset_graph(ax, max_annot):
    global i, max_value
    # Réinitialiser le graphique
    ax.clear()
    # Réinitialiser les limites de l'axe des x
    ax.set_xlim(left=0, right=1)
    # Réinitialiser les limites de l'axe des y
    ax.set_ylim(bottom=0, top=1)
    # Réinitialiser la valeur maximale
    max_value = 0
    # Réinitialiser l'annotation de la valeur maximale
    max_annot.set_text('')
    # Réinitialiser le compteur d'itérations
    i = 0
    # Rafraîchir le graphique
    fig.canvas.draw()
