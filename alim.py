import requests
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt

url = 'http://192.168.0.2/Home.cgi'
i=0

# Crée une figure et un sous-plot
fig, ax = plt.subplots()

# Crée une ligne vide
line, = ax.plot([], [])

while True:
    response = requests.get(url)
    if response.status_code == 200:
        #Extrait la valeur à partir du contenu de la page web
        soup = BeautifulSoup(response.text, 'html.parser')

        #Trouver l'input avec l'attribut id "actcur"
        input_element = soup.find('input', {'id':'actcur'})

        #Extrait la valeur de l'attribut "value"
        value = float(input_element['value'].replace(' A', ''))

        # Met à jour la ligne avec les nouvelles données
        line.set_data([i], [value])

        # Met à jour les limites de l'axe des x
        ax.set_xlim([i-50, i])

        # Met à jour les limites de l'axe des y
        ax.set_ylim([min(value, value-0.1), max(value, value+0.1)])

        # Rafraîchit la fenêtre graphique
        fig.canvas.draw()
        fig.canvas.flush_events()

        print(i,value)
        i+=1
    else:
        print(f"Erreur {response.status_code} lors de la récupération de la page web de l'alimentation")

    # Attend une seconde avant la prochaine requête
    time.sleep(1)
