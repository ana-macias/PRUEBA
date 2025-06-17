from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from fake_useragent import UserAgent
url = "https://www.imdb.com/chart/top/"
ua = UserAgent()
headers = {'User-Agent': ua.random}
response = requests.get(url, headers=headers)
htlm = response.text
soup = bs(htlm,'html.parser') 

# He encontrado estos Selectores actualizados para 2023 porque me estaba volviendo loca!!!
movie_list = soup.select('li.ipc-metadata-list-summary-item')
    
pelis = []
for movie in movie_list:
   
    posicion = movie.select_one('h3.ipc-title__text').get_text(strip=True).split('.')[0]  # Para encontrar la posición
         
    titulo = movie.select_one('h3.ipc-title__text').get_text(strip=True).split('.')[1].strip() # Para encontar el título  
    
    metadata = movie.select_one('div.cli-title-metadata') 
   
    año = metadata.find_all('span')[0].text # Para el año 
    
    duracion = metadata.find_all('span')[1].text if len(metadata.find_all('span')) > 1 else "N/A" # Para la duración
        
    puntuacion = movie.select_one('span.ipc-rating-star').get_text(strip=True).split()[0] # Para el rating
        
    pelis.append({
        'Posición': posicion,
        'Título': titulo,
        'Año': año, 
        'Duración': duracion,
        'Rating': puntuacion
        })

# Crear DataFrame y guardar CSV
df = pd.DataFrame(pelis)
df.to_csv('top250_imdb_actualizado.csv', index=False)
print(df)
# CON ESTA OPCION SOLO OBTENEMOS 25 VALORES