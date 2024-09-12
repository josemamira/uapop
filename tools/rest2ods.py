import requests
from odf.opendocument import OpenDocumentSpreadsheet
# instalar odfpy usando "pip install odfpy"
from odf.table import Table, TableRow, TableCell
from odf.text import P

# URL de la API que devuelve datos en formato JSON
url = "https://api.wallapop.com/api/v3/search?source=quick_filters&keywords=lamparas&latitude=38.38277636&longitude=-0.51136203&order_by=closest&distance_in_km=10&search_id=fa63a7d2-a30f-4769-8d9b-80ec3c2da039&show_multiple_sections=false"


# Realiza la solicitud GET para obtener el JSON
response = requests.get(url)
data = response.json()

# Extrae los ítems del JSON
items = data["data"]["section"]["payload"]["items"]

# Crea un nuevo documento ODS
spreadsheet = OpenDocumentSpreadsheet()

# Crea una tabla dentro del documento
table = Table(name="Resultados")

# Añade una fila de encabezados
headers = ["id", "user_id", "title", "description", "longitude", "latitude", "price", "postal_code", "region", "image","category_id","taxonomy_1"]
header_row = TableRow()
for header in headers:
    cell = TableCell()
    cell.addElement(P(text=header))
    header_row.addElement(cell)
table.addElement(header_row)

# Añade una fila por cada ítem en los resultados
for item in items:
    row = TableRow()

    # Extrae los campos necesarios
    id_ = item.get("id", "")
    user_id = item.get("user_id", "")
    title = item.get("title", "")
    description = item.get("description", "")
    longitude = item["location"].get("longitude", "")
    latitude = item["location"].get("latitude", "")
    price = item["price"].get("amount", "")
    postal_code = item["location"].get("postal_code", "")
    region = item["location"].get("region", "")
    category_id = item.get("category_id", "")
    taxonomy_1 = item["taxonomy"][0].get("name", "")
    #taxonomy_2 = item["taxonomy"][1].get("name", "")
    #taxonomy_3 = item["taxonomy"][2].get("name", "")
    
    
    # Concatenamos las URL de las imágenes en un solo campo
    #images = ", ".join([img["urls"]["big"] for img in item["images"]])
    # obtener la primera imagen
    image = item['images'][0]['urls']['small']  # Solo la primera imagen

    # Crea celdas para cada campo
    fields = [id_, user_id, title, description, longitude, latitude, price, postal_code, region, image, category_id, taxonomy_1]
    for field in fields:
        cell = TableCell()
        cell.addElement(P(text=str(field)))
        row.addElement(cell)

    # Añade la fila a la tabla
    table.addElement(row)

# Añade la tabla al documento
spreadsheet.spreadsheet.addElement(table)

# Guarda el archivo ODS
spreadsheet.save("resultados.ods")
print("Archivo ODS generado: resultados.ods")