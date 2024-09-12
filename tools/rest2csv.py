import requests
import csv

# URL de la API
url = "https://api.wallapop.com/api/v3/search?source=quick_filters&keywords=lamparas&latitude=38.38277636&longitude=-0.51136203&order_by=closest&distance_in_km=10&search_id=fa63a7d2-a30f-4769-8d9b-80ec3c2da039&show_multiple_sections=false"

# Realizar la solicitud HTTP
response = requests.get(url)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()

    # Extraer la lista de productos desde el JSON
    products = data["data"]["section"]["payload"]["items"]

    # Nombre del archivo CSV de salida
    output_file = "productos.csv"

    # Definir las columnas que tendrá el archivo CSV
    headers = ["id", "user_id", "title", "description", "price", "latitude", "longitude", "postal_code", "region", "images"]

    # Crear el archivo CSV y escribir los datos
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

        # Iterar sobre cada producto y extraer los campos necesarios
        for product in products:
            # Procesar las imágenes: si hay más de una, las concatenamos
            images = ", ".join([img["urls"]["big"] for img in product["images"]])

            # Crear el diccionario con los campos que queremos
            row = {
                "id": product["id"],
                "user_id": product["user_id"],
                "title": product["title"],
                "description": product["description"],
                "price": product["price"]["amount"],                
                "latitude": product["location"]["latitude"],
                "longitude": product["location"]["longitude"],
                "postal_code": product["location"]["postal_code"],
                "region": product["location"]["region"],
                "images": images
            }

            # Escribir la fila en el CSV
            writer.writerow(row)

    print(f"Archivo CSV '{output_file}' creado exitosamente.")

else:
    print(f"Error en la solicitud HTTP: {response.status_code}")
