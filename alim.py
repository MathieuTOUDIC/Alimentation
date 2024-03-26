import tkinter as tk
import requests
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.widgets import SpanSelector

url = 'http://192.168.0.2/Home.cgi'
i = 0
max_value = 0

# Activer le mode interactif de Matplotlib
plt.ion()

# Créer une figure et un graphique
fig, ax = plt.subplots()

# Ajouter une annotation vide pour la valeur maximale
max_annot = ax.text(0.05, 0.9, '', transform=ax.transAxes)

# Définir un format personnalisé pour les étiquettes des graduations de l'axe des x
def format_x(x, pos):
    minutes = int(x / 60)
    seconds = int(x % 60)
    if seconds == 0:
        return f'{minutes} m{""}'
    else:
        return f'{minutes} m{""} {seconds} s{""}'

formatter = ticker.FuncFormatter(format_x)
ax.xaxis.set_major_formatter(formatter)

# Créer une fenêtre Tkinter
window = tk.Tk()
window.title("Graphique")

# Créer un bouton de réinitialisation
reset_button = tk.Button(window, text="Réinitialiser le graphique", command=lambda: reset_graph(ax, max_annot))
reset_button.pack()

# Créer le widget SpanSelector pour le zoom
span = SpanSelector(ax, onselect=lambda xmin, xmax: ax.set_xlim(xmin, xmax), rectprops=dict(facecolor='red', alpha=0.5))

# Fonction de rappel pour le bouton de réinitialisation
def reset_graph(ax, max_annot):
    global i, max_value
    # Réinitialiser le graphique
    ax.clear()
    # Réinitialiser les limites de l'axe des x
    ax.set_xlim(left=0, right=i+1)
    # Réinitialiser les limites de l'axe des y
    ax.set_ylim(bottom=0, top=max_value)
    # Réinitialiser la valeur maximale
    max_value = 0
    # Réinitialiser l'annotation de la valeur maximale
    max_annot.set_text('')
    # Réinitialiser la variable i
    i = 0
    # Rafraîchir le graphique
    fig.canvas.draw()
    fig.canvas.flush_events()

# Boucle principale du graphique
while True:
    response = requests.get(url)
    if response.status_code == 200:
        #Extrait la valeur à partir du contenu de la page web
        soup = BeautifulSoup(response.text, 'html.parser')

        #Trouver l'input avec l'attribut id "actcur"
        input_element = soup.find('input', {'id':'actcur'})

        #Extrait la valeur de l'attribut "value"
        value = input_element['value']

        # Mettre à jour la valeur maximale si nécessaire
        max_value = max(max_value, float(value.replace(' A', '')))

        # Ajouter la valeur au graphique
        ax.plot(i, float(value.replace(' A', '')), 'bo')

        # Définir les limites de l'axe des x
        ax.set_xlim(left=0, right=i+1)

        # Définir les limites de l'axe des y
        ax.set_ylim(bottom=0, top=max_value)

        # Ajouter des graduations sur l'axe des y
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))

        # Mettre à jour le texte de l'annotation de la valeur maximale
        max_annot.set_text(f'Max: {max_value:.2f} A')

        # Rafraîchir le graphique
        fig.canvas.draw()
        fig.canvas.flush_events()

        print(i, value)
        i += 1
    else:
        print(f"Erreur {response.status_code} lors de la récupération de la page web de l'alimentation")

    # Attend une seconde avant la prochaine requête
    time.sleep(1)

# Boucle principale de Tkinter
window.mainloop()
