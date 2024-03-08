import matplotlib.pyplot as plt

# Créer des données pour le graphique
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Créer une figure et un graphique
fig, ax = plt.subplots()

# Ajouter les données au graphique
ax.plot(x, y)

# Définir les titres des axes
ax.set_xlabel('Titre de l\'axe des x')
ax.set_ylabel('Titre de l\'axe des y')
ax.set_title('Titre du graphique')

# Afficher le graphique
plt.show()
