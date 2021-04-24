#Pasos Previos
## 1. Descargar requests para python3 en venv => pip3 install requests. Sirve para descargar webpages
## 2. Descargar bs4 en venv
import requests
from bs4 import BeautifulSoup as bs

# crear variable que recolecta el usuario de Github
github_user = input(f'Tell me your Github user: ')

#First step: to send a request to the URL i want to scrap... i need an URL => Creo la url que quiero scrappear
url = 'https://github.com/'+github_user
#Second Step: Send the request. 
r = requests.get(url) #Esta función envia un request a la URL que acabamos de especificar
#Third step: Vamos a recolectar el HTML de la página
soup = bs(r.content, 'html.parser') #la variable soup almacena todo el HTML de la página
#Fourth Step: Especificar qué tag necesitamos traer del HTML
profile_img = soup.find('img', {'class':'avatar avatar-user width-full border color-bg-primary'})['src']
#Muestro la URL para que la persona le de click
print(f'Esta es la URL de: '+ profile_img)