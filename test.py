import tkinter as tk

# Créer une fenêtre principale
window = tk.Tk()

# Définir le titre de la fenêtre
window.title("Ma fenêtre Tkinter")

# Créer un bouton
button = tk.Button(window, text="Cliquez-moi !", command=lambda: print("Bonjour !"))

# Ajouter le bouton à la fenêtre
button.pack()

# Créer un message
label = tk.Label(window, text="Salut, bienvenue dans ma fenêtre Tkinter !")

# Ajouter le message à la fenêtre
label.pack()

# Démarrer la boucle principale de Tkinter
window.mainloop()
