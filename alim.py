import requests
from bs4 import BeautifulSoup
import time

url = 'http://192.168.0.2/Home.cgi'
i=0
while True:
    response = requests.get(url)
    if response.status_code == 200:
        #Extrait la valeur à partir du contenu de la page web
        soup = BeautifulSoup(response.text, 'html.parser')

        #Trouver l'input avec l'attribut id "actcur"
        input_element = soup.find('input', {'id':'actcur'})

        #Extrait la valeur de l'attribut "value"
        value = input_element['value']

        print(i,value)
        i+=1
    else:
        print(f"Erreur {response.status_code} lors de la récupération de la page wed de l'alimentation")

    # Attend une seconde avant la prohaine requête 
    time.sleep(1)