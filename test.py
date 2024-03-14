import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Ma fenêtre graphique")

# Création d'une variable
ma_variable = tk.IntVar()

# Création d'un bouton
bouton = tk.Button(fenetre, text="Cliquez-moi !", command=lambda: ma_variable.set(ma_variable.get() + 1))
bouton.pack()

# Création d'un afficheur de variable
afficheur = tk.Label(fenetre, textvariable=ma_variable)
afficheur.pack()

# Création d'un graphique
figure = plt.Figure(figsize=(5, 4), dpi=100)
axes = figure.add_subplot(111)
x = np.linspace(0, 10, 100)
y = np.sin(x)
axes.plot(x, y)

# Ajout du graphique à la fenêtre
canvas = FigureCanvasTkAgg(figure, fenetre)
canvas.draw()
canvas.get_tk_widget().pack()

# Boucle principale de l'interface graphique
fenetre.mainloop()
