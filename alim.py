url = 'http://192.168.0.2/Home.cgi'
time_sec = 0  # Ajouter une variable pour stocker le temps en secondes
max_value = 0  # Ajouter une variable pour stocker la valeur maximale

# Activer le mode interactif de Matplotlib
plt.ion()

# Créer une figure et un graphique
fig, ax = plt.subplots()

# Ajouter une annotation vide pour la valeur maximale
max_annot = ax.text(0.05, 0.9, '', transform=ax.transAxes)

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
        ax.plot(time_sec / 60, float(value.replace(' A', '')), 'bo')  # Convertir le temps en minutes

        # Définir les limites de l'axe des x
        ax.set_xlim(left=0, right=(time_sec+1) / 60)  # Convertir le temps en minutes

        # Définir les limites de l'axe des y
        ax.set_ylim(bottom=0, top=max_value+1)

        # Mettre à jour le texte de l'annotation de la valeur maximale
        max_annot.set_text(f'Max: {max_value:.2f} A')

        # Rafraîchir le graphique
        fig.canvas.draw()
        fig.canvas.flush_events()

        print(time_sec / 60, value)  # Convertir le temps en minutes
        time_sec += 1  # Incrémenter le temps de 1 seconde
    else:
        print(f"Erreur {response.status_code} lors de la récupération de la page web de l'alimentation")

    # Attend une seconde avant la prochaine requête
    time.sleep(1)
