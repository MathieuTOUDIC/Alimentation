import matplotlib.pyplot as plt
import time
import requests
from bs4 import BeautifulSoup

# fonction pour récupérer la valeur à partir de la page web
def get_value():
    url = "http://example.com/page.html"
    response = requests.get(url)
    #Extrait la valeur à partir du contenu de la page web
    soup = BeautifulSoup(response.text, 'html.parser')
    
    #Trouver l'input avec l'attribut id "actcur"
    input_field = soup.find('input', {'id':'actcur'})
    if input_field is not None:
        value = input_field["value"]
    else:
        value = None

    print(value)
    return float(value.replace(" A", ""))

# créer un graphique ligne vide
fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_ylim(0, 1)

# boucle infinie pour mettre à jour le graphique en temps réel
while True:
    # récupérer la nouvelle valeur à partir de la page web
    value = get_value()

    # mettre à jour les données du graphique
    line.set_data([value], [value])
    ax.set_xlim(value-0.01, value+0.01)

    # redessiner le graphique
    fig.canvas.draw()
    fig.canvas.flush_events()

    # attendre une seconde avant la prochaine mise à jour
    time.sleep(1)