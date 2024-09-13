[En español en este mismo documento](#Español)

# UAPOP: Tools for make web maps using Wallapop Rest API

This project aims to show some examples of using the Wallapop REST API to generate web maps using [MapLibre GL JS](https://github.com/maplibre/maplibre-gl-js). It also includes some Python utilities to convert API requests into formats such as Excel (XLS), CSV, GeoJSON or LibreOffice Calc (ODS).

### DEMO

Demo HTML pages using Maplibre GL JS

- [Geojson in html code: test1_geojson_text.html](https://josemamira.github.io/uapop/maplibre/test1_geojson_text.html)
- [Geojson from URL link:  test2_geojson_url.html](https://josemamira.github.io/uapop/maplibre/test2_geojson_url.html)
- [REST to map:  rest2map.html](https://josemamira.github.io/uapop/maplibre/rest2map.html)
- [REST to map with form:  rest2map_form.html](https://josemamira.github.io/uapop/maplibre/rest2map_form.html)
- [REST to map with form and icons:  rest2map_form_icons.html](https://josemamira.github.io/uapop/maplibre/rest2map_form_icons.html)

Date: 11 septiembre 2024

Wallapop has an API that can be consulted using a web browser

### See categories:

https://api.wallapop.com/api/v3/categories

### Search
To find an example, open Wallapop in your browser (Chrome) and search for what you want with the desired criteria (name, distance, order, price, etc.)

Enter developer mode (Ctrl + i) and then look in the "Network" tab for a row that says "search?source=...". Select the row and right-click to open it in a new tab.


Main URL: https://api.wallapop.com/api/v3/general/search"

PARAMETERS (with examples):

    - filters_source: search_box,
    - min_sale_price: 120,
    - max_sale_price: 300
    - order_by= closest | most_relevance
    - source=quick_filter
    - keywords= smartwatch | biciclete%20mtb
    - category_id=24200
    - latitude=38.38277636
    - longitude=-0.51136203  
    - distance_in_km=1
    
#### EXEMPLES | EJEMPLOS:

MTB Bike order by distance | Bicicleta MTB ordenado por distancia. 

[https://api.wallapop.com/api/v3/search?source=quick_filters&keywords=bicicleta%20mtb&latitude=38.38277636&longitude=-0.51136203&order_by=closest](https://api.wallapop.com/api/v3/search?source=quick_filters&keywords=bicicleta%20mtb&latitude=38.38277636&longitude=-0.51136203&order_by=closest)


Bike under 500 € | Bicicleta de menos de 500 €

[https://api.wallapop.com/api/v3/search?source=search_box&keywords=bicicleta%20mtb&latitude=38.38277636&longitude=-0.51136203&order_by=closest&max_sale_price=500](https://api.wallapop.com/api/v3/search?source=search_box&keywords=bicicleta%20mtb&latitude=38.38277636&longitude=-0.51136203&order_by=closest&max_sale_price=500)

Search bikes between €400 and €500 in Alicante | Buscar bicicletas entre 400 y 500 € en Alicante

[https://api.wallapop.com/api/v3/search?source=search_box&keywords=bicicleta%20mtb&latitude=38.38277636&longitude=-0.51136203&order_by=closest&min_sale_price=300&max_sale_price=500](https://api.wallapop.com/api/v3/search?source=search_box&keywords=bicicleta%20mtb&latitude=38.38277636&longitude=-0.51136203&order_by=closest&min_sale_price=300&max_sale_price=500)

Smartwatch under €50 from the Watches category, less than 1 km away | Smartwatch de menos de 50€ de la categoría Relojes, a menos de 1 km

[https://api.wallapop.com/api/v3/search?source=quick_filters&keywords=smartwatch&category_id=24200&latitude=38.38277636&longitude=-0.51136203&max_sale_price=100](https://api.wallapop.com/api/v3/search?source=quick_filters&keywords=smartwatch&category_id=24200&latitude=38.38277636&longitude=-0.51136203&max_sale_price=100)

### TOOLS:

These utilities are programmed in python. You need install this libs 

- geojson
- odfpy 

How to install ?

> pip install geojson
> pip install odfpy
> pip install requests pandas openpyxl

Run in a terminal by typing:

> python3 <file.py>

Python files:

- rest2ods.py: generates a table in a LibreOffice Calc (ods) file with the result
- rest2xls.py: generates a table in an Excel file with the result
- rest2geojson.py: generates a geojson file with the result
- rest2csv.py: generates a table in a CSV file with the result
  

NOTE: In each file you have to change the line with the URL so that it works with other criteria: position, text, etc.







## Español
# UAPOP: Utilidades para crear mapas web usando el API REST de Wallapop

Este proyecto pretende mostrar algunos ejemplos de uso del API REST de Wallapop para generar mapas web usando MapLibre GL JS. También incluye algunas utilidades en Python para convertir las peticiones de la API en formatos como Excel (XLS), CSV, GeoJSON o LibreOffice Calc (ODS)

Fecha documento: 11 septiembre 2024

Wallapop tiene una API que se puede consultar, por ejemplo vía navegador

### Ver categorías:

https://api.wallapop.com/api/v3/categories

### Buscar 

Para buscar un ejemplo abre wallapop en el navegador (Chrome) y busca lo que quieras con los criterios deseados (nombre, distancia, orden, precio, etc.)

Entra en modo desarrollador (Ctrl + i) y luego busca en la pestaña "Network" una fila que ponga "search?source=...". Selecciona la fila y con el botón derecho ábrelo en una nueva pestaña

URL principal: https://api.wallapop.com/api/v3/general/search"

PARÁMETROS (con ejemplo):

    - filters_source: search_box,
    - min_sale_price: 120,
    - max_sale_price: 300
    - order_by= closest | most_relevance
    - source=quick_filter
    - keywords= smartwatch | biciclete%20mtb
    - category_id=24200
    - latitude=38.38277636
    - longitude=-0.51136203  
    - distance_in_km=1
    
#### EJEMPLOS:

Bicicleta MTB ordenado por distancia. 

[https://api.wallapop.com/api/v3/search?source=quick_filters&keywords=bicicleta%20mtb&latitude=38.38277636&longitude=-0.51136203&order_by=closest](https://api.wallapop.com/api/v3/search?source=quick_filters&keywords=bicicleta%20mtb&latitude=38.38277636&longitude=-0.51136203&order_by=closest)

Bicicleta de menos de 500 €

[https://api.wallapop.com/api/v3/search?source=search_box&keywords=bicicleta%20mtb&latitude=38.38277636&longitude=-0.51136203&order_by=closest&max_sale_price=500](https://api.wallapop.com/api/v3/search?source=search_box&keywords=bicicleta%20mtb&latitude=38.38277636&longitude=-0.51136203&order_by=closest&max_sale_price=500)

Buscar bicicletas entre 400 y 500 € en Alicante

[https://api.wallapop.com/api/v3/search?source=search_box&keywords=bicicleta%20mtb&latitude=38.38277636&longitude=-0.51136203&order_by=closest&min_sale_price=300&max_sale_price=500](https://api.wallapop.com/api/v3/search?source=search_box&keywords=bicicleta%20mtb&latitude=38.38277636&longitude=-0.51136203&order_by=closest&min_sale_price=300&max_sale_price=500)

Smartwatch de menos de 50€ de la categoría Relojes, a menos de 1 km

[https://api.wallapop.com/api/v3/search?source=quick_filters&keywords=smartwatch&category_id=24200&latitude=38.38277636&longitude=-0.51136203&max_sale_price=100](https://api.wallapop.com/api/v3/search?source=quick_filters&keywords=smartwatch&category_id=24200&latitude=38.38277636&longitude=-0.51136203&max_sale_price=100)


### UTILIDADES:

Estas utilidades están programadas en python

Se necesitan instalar las librerías

- geojson
- odfpy 

Instala las librerías:

> pip install geojson
> pip install odfpy
> pip install requests pandas openpyxl

 Se ejecutan en una terminal escribiendo

> python3 <fichero.py>

Ficheros Python:
 
- rest2ods.py: genera una tabla en un archivo de LibreOffice Calc (ods) con el resultado
- rest2xls.py: genera una tabla en un archivo de Excel con el resultado
- rest2geojson.py: genera una archivo geojson con el resultado
- rest2csv.py: genera una tabla en un archivo de CSV con el resultado

NOTA: En cada fichero hay que cambiar la línea con la URL para que funcione con otros criterios: posición, texto, etc.


### DEMO

Ejemplos web usando Maplibre GL JS

- [Geojson in html code: test1_geojson_text.html](https://josemamira.github.io/uapop/maplibre/test1_geojson_text.html)
- [Geojson from URL link:  test2_geojson_url.html](https://josemamira.github.io/uapop/maplibre/test2_geojson_url.html)
- [REST to map:  rest2map.html](https://josemamira.github.io/uapop/maplibre/rest2map.html)
- [REST to map with form:  rest2map_form.html](https://josemamira.github.io/uapop/maplibre/rest2map_form.html)




