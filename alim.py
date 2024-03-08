import requests
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt

url = 'http://192.168.0.2/Home.cgi'
i = 0

# Activer le mode interactif de Matplotlib
plt.ion()

# Créer une figure et un graphique
fig, ax = plt.subplots()

while True:
    response = requests.get(url)
    if response.status_code == 200:
        #Extrait la valeur à partir du contenu de la page web
        soup = BeautifulSoup(response.text, 'html.parser')

        #Trouver l'input avec l'attribut id "actcur"
        input_element = soup.find('input', {'id':'actcur'})

        #Extrait la valeur de l'attribut "value"
        value = input_element['value']

        # Ajouter la valeur au graphique
        ax.plot(i, float(value.replace(' A', '')), 'bo')

        # Définir les limites de l'axe des x
        ax.set_xlim(left=0, right=i+1)

        # Définir les limites de l'axe des y
        ax.set_ylim(bottom=0, top=max(float(value.replace(' A', '')), 1))

        # Rafraîchir le graphique
        fig.canvas.draw()
        fig.canvas.flush_events()

        print(i, value)
        i += 1
    else:
        print(f"Erreur {response.status_code} lors de la récupération de la page web de l'alimentation")

    # Attend une seconde avant la prochaine requête
    time.sleep(1)
