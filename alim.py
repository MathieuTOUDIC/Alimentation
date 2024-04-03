import tkinter as tk
import requests
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import collections

url = 'http://192.168.0.2/Home.cgi'
i = 0
max_value = 0
change_color = False  # Ajouter une variable booléenne pour changer la couleur des points

# Activer le mode interactif de Matplotlib
plt.ion()

# Créer une figure et un graphique
fig, ax = plt.subplots()

fig.suptitle('Appuyer sur c pour changer la couleur des points', y=0.05)

# Ajouter une grille au graphique
ax.grid(which='major', linestyle='--', linewidth=0.5, color='gray')

# Ajouter une annotation vide pour la valeur maximale
max_annot = ax.text(0.05, 1.01, '', transform=ax.transAxes)

# Définir un format personnalisé pour les étiquettes des graduations de l'axe des x
def format_x(x, pos):
    seconds = int(x)  # Convertir les secondes en entier

    minutes = int(seconds / 60)
    seconds = int(seconds % 60)

    if minutes > 0:
        if seconds > 0:
            return f'{minutes}m {seconds}s'
        else:
            return f'{minutes}m'
    elif seconds > 0:
        return f'{seconds}s'
    else:
        return ''

# Formater les étiquettes des graduations de l'axe des x
ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_x))

# Définir les intervalles entre les graduations de l'axe des x
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

# Définir une fonction de rappel pour afficher le curseur lorsque la touche c est appuyée
def on_key_press(event):
    global change_color  # Utiliser la variable globale change_color
    if event.key == 'c':
        change_color = not change_color  # Basculer la valeur de change_color

# Connecter la fonction de rappel à l'événement de pression de touche
fig.canvas.mpl_connect('key_press_event', on_key_press)

# Définir l'intervalle de temps entre deux requêtes (en secondes)
time_interval = 1

# Mesurer le temps écoulé depuis le début du programme
start_time = time.perf_counter()

# Définir la taille de la liste circulaire (nombre de valeurs à afficher sur l'axe des x)
buffer_size = 60

# Créer une liste circulaire pour stocker les valeurs de puissance
power_buffer = collections.deque(maxlen=buffer_size)

# Boucle principale du graphique
while True:
    # Mesurer le temps écoulé depuis la dernière requête
    elapsed_time = time.perf_counter() - start_time

    response = requests.get(url)
    if response.status_code == 200:
        #Extrait la valeur à partir du contenu de la page web
        soup = BeautifulSoup(response.text, 'html.parser')

        #Trouver l'input avec l'attribut id "actcur"
        current_element = soup.find('input', {'id':'actcur'})

        #Trouver l'input avec l'attribut id "actvol"
        voltage_element = soup.find('input', {'id':'actvol'})

        #Extrait la valeur du courant de l'attribut "value" et conversion en float
        current = float(current_element['value'].replace(' A', ''))

        #Extrait la valeur de la tension de l'attribut "value" et conversion en float
        voltage = float(voltage_element['value'].replace(' V', ''))

        #Multiplication du courant par la tension pour avoir la puissance
        power = current*voltage

        # Mettre à jour la valeur maximale si nécessaire
        max_value = max(max_value, power)

        # Ajouter la valeur au buffer circulaire
        power_buffer.append(power)

        # Effacer le graphique
        ax.clear()

        # Ajouter une grille au graphique
        ax.grid(which='major', linestyle='--', linewidth=0.5, color='gray')

        # Ajouter les valeurs du buffer circulaire au graphique
        ax.plot(range(len(power_buffer)), power_buffer, color=color, marker='o', markersize=1)

        # Définir les limites de l'axe des x
        ax.set_xlim(left=0, right=len(power_buffer))

        # Définir les limites de l'axe des y
        ax.set_ylim(bottom=0, top=max_value)

        # Ajouter des graduations sur l'axe des y
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))

        # Mettre à jour le texte de l'annotation de la valeur maximale
        max_annot.set_text(f'Max: {max_value:.2f} W')

        # Rafraîchir le graphique
        fig.canvas.draw()
        fig.canvas.flush_events()

        print(elapsed_time, power)
    else:
        print(f"Erreur {response.status_code} lors de la récupération de la page web de l'alimentation")

    # Attendre l'intervalle de temps entre deux requêtes
    time.sleep(time_interval)


# Boucle principale de Tkinter
window.mainloop()
