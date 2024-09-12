import requests
import pandas as pd

# instalar las librerías 
# pip install requests pandas openpyxl

# URL de la API (puedes cambiarla por la correcta)
url = "https://api.wallapop.com/api/v3/search?source=quick_filters&keywords=lamparas&latitude=38.38277636&longitude=-0.51136203&order_by=closest&distance_in_km=10&search_id=fa63a7d2-a30f-4769-8d9b-80ec3c2da039&show_multiple_sections=false"

# Hacemos la petición GET a la URL
response = requests.get(url)

# Verificamos si la petición fue exitosa
if response.status_code == 200:
    # Extraemos el JSON de la respuesta
    data = response.json()

    # Accedemos a los items en el JSON
    items = data['data']['section']['payload']['items']
    
    # Creamos una lista para almacenar los datos
    data_list = []

    # Iteramos sobre los items para extraer los datos necesarios
    for item in items:
        item_data = {
            'id': item['id'],
            'user_id': item['user_id'],
            'title': item['title'],
            'description': item['description'],
            'longitude': item['location']['longitude'],
            'latitude': item['location']['latitude'],
            'price': item['price']['amount'],
            'postal_code': item['location']['postal_code'],
            'region': item['location']['region'],
            'images': item['images'][0]['urls']['big'] if item['images'] else None
        }
        data_list.append(item_data)

    # Convertimos la lista de datos en un DataFrame de pandas
    df = pd.DataFrame(data_list)

    # Guardamos el DataFrame en un archivo Excel
    df.to_excel('resultado.xlsx', index=False)

    print('Archivo Excel creado exitosamente.')

else:
    print(f'Error en la solicitud. Código de estado: {response.status_code}')
    

