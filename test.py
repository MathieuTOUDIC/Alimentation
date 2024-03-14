import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class GraphicInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface graphique")

        # Créer un canvas pour le graphique
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Créer un emplacement pour afficher la valeur maximale
        self.max_value_label = tk.Label(root, text="Valeur maximale : ")
        self.max_value_label.pack(side=tk.TOP)

        # Créer un bouton de réinitialisation
        self.reset_button = tk.Button(root, text="Réinitialiser", command=self.reset_graph)
        self.reset_button.pack(side=tk.BOTTOM)

        # Créer le graphique initial
        self.create_graph()

    def create_graph(self):
        # Générer des données aléatoires
        x = np.linspace(0, 10, 100)
        y = np.sin(x) * np.random.rand() + np.random.rand()

        # Effacer les anciens graphiques
        for ax in self.figure.get_axes():
            self.figure.remove(ax)

        # Créer un nouvel axe et tracer le graphique
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)

        # Calculer et afficher la valeur maximale
        max_value = np.max(y)
        self.max_value_label.config(text=f"Valeur maximale : {max_value:.2f}")

        # Redessiner le canvas
        self.canvas.draw()

    def reset_graph(self):
        self.create_graph()

if __name__ == "__main__":
    root = tk.Tk()
    gui = GraphicInterface(root)
    root.mainloop()
