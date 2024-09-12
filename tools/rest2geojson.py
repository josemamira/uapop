import requests
import json
# recuerda instalar  geojson con "pip install geojson"
import geojson

# URL de la API que devuelve datos en formato JSON
url = "https://api.wallapop.com/api/v3/search?source=quick_filters&keywords=bicicleta%20mtb&latitude=38.38277636&longitude=-0.51136203&order_by=closest&distance_in_km=10&search_id=fa63a7d2-a30f-4769-8d9b-80ec3c2da039&show_multiple_sections=false"

# Realiza la solicitud
response = requests.get(url)
data = response.json()

# Extraer los items
items = data["data"]["section"]["payload"]["items"]

# Crear lista de características GeoJSON
features = []

for item in items:
    # Extraer las propiedades necesarias
    feature = geojson.Feature(
        geometry=geojson.Point((item["location"]["longitude"], item["location"]["latitude"])),
        properties={
            "id": item["id"],
            "user_id": item["user_id"],
            "title": item["title"],
            "description": item["description"],
            "category_id": item["category_id"],
            "price": f'{item["price"]["amount"]} {item["price"]["currency"]}',
            #"images": [img["urls"]["big"] for img in item["images"]],
            "image" : item["images"][0]["urls"]["small"],
            "postal_code": item["location"]["postal_code"],
            "region": item["location"]["region"]
        }
    )
    features.append(feature)

# Crear el objeto GeoJSON final
geojson_data = geojson.FeatureCollection(features)

# Guardar el archivo GeoJSON
with open('items.geojson', 'w') as geojson_file:
    geojson.dump(geojson_data, geojson_file, indent=2)

print("Archivo GeoJSON generado: items.geojson")
