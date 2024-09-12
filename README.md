# UAPOP: Tools for make maps using Wallapop Rest API

Demo HTML pages using Maplibre GL JS

- [Geojson in html code: test1_geojson_text.html](https://josemamira.github.io/uapop/maplibre/)
- [Geojson from URL link:  test2_geojson_url.html](https://josemamira.github.io/uapop/maplibre/test2_geojson_url.html)

Fecha documento: 11 septiembre 2024

Wallapop tiene una API que se puede consultar, por ejemplo vía navegador

### Ver categorías:

https://api.wallapop.com/api/v3/categories

### Buscar 
Para buscar un ejemplo abre wallapop en el navegador (Chrome) y busca lo que quieras con los criterios deseados (nombre, distancia, orden, precio, etc.)

Entra en modo desarrollador (Ctrl + i) y luego busca en la pestaña "Network" una fila que ponga "search?source=...". Selecciona la fila y con el botón derecho ábrelo en una nueva pestaña

URL: https://api.wallapop.com/api/v3/general/search"

PARÁMETROS (con ejemplo):

    "keywords": "ordenador",
    "filters_source": "search_box",
    "min_sale_price": 120,
    "max_sale_price": 300
    "latitude": "38.389175",
    "longitude": "-0.5163323",   
    order_by= closest | most_relevance
    source=quick_filter
    keywords= smartwatch | biciclete%20mtb
    category_id=24200
    latitude=38.38277636
    longitude=-0.51136203  
    distance_in_km=1
    
#### EJEMPLOS:

Bicicleta MTB ordenado por distancia. 

https://api.wallapop.com/api/v3/search?source=quick_filters&keywords=bicicleta%20mtb&latitude=38.38277636&longitude=-0.51136203&order_by=closest

Bicicleta de menos de 500 €

https://api.wallapop.com/api/v3/search?source=search_box&keywords=bicicleta%20mtb&latitude=38.38277636&longitude=-0.51136203&order_by=closest&max_sale_price=500

Buscar bicicletas entre 400 y 500 € en Alicante

https://api.wallapop.com/api/v3/search?source=search_box&keywords=bicicleta%20mtb&latitude=38.38277636&longitude=-0.51136203&order_by=closest&min_sale_price=300&max_sale_price=500

smartwatch de menos de 50€ de la categoría Relojes, a menos de 1 km

https://api.wallapop.com/api/v3/search?source=quick_filters&keywords=smartwatch&category_id=24200&latitude=38.38277636&longitude=-0.51136203&max_sale_price=100


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

Abre el fichero maplibre.html con un navegador y comprueba el resultado

Puedes personalizarlo copiando y pegando el texto de tu geojson


Código fuente:
```javascript
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MapLibre con GeoJSON y Popups</title>
    <script src="https://unpkg.com/maplibre-gl@latest/dist/maplibre-gl.js"></script>
    <link href="https://unpkg.com/maplibre-gl@latest/dist/maplibre-gl.css" rel="stylesheet" />
    <style>
        body { margin: 0; padding: 0; }
        #map { position: absolute; top: 0; bottom: 0; width: 100%; }
        .popup-content img { max-width: 200px; max-height: 200px; }
    </style>
</head>
<body>

<div id="map"></div>

<script>
    // Inicializa el mapa
    const key = 'FarArRCYRxNEd0LV6d95';
    const map = new maplibregl.Map({
        container: 'map', // ID del contenedor
        style: 'https://api.maptiler.com/maps/streets/style.json?key='+key, // URL de estilo de MapLibre
        center: [-0.51, 38.38], // Coordenadas iniciales [longitud, latitud]
        zoom: 12 // Nivel de zoom inicial
    });

    // Añadir controles de zoom y rotación al mapa
    map.addControl(new maplibregl.NavigationControl());

    // Fichero GeoJSON con los puntos
    const geojson = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -0.519802,
          38.383981
        ]
      },
      "properties": {
        "id": "3zl85g38026x",
        "user_id": "dqjwdx5rekzo",
        "title": "Lampara mesilla",
        "description": "lampara medilla 58cm de alto",
        "price": "10.0 EUR",
        "image": "https://cdn.wallapop.com/images/10420/h9/ky/__/c10420p1044019193/i5101472212.jpg?pictureSize=W320",
        "postal_code": "03690",
        "region": "Comunidad Valenciana"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -0.519802,
          38.383981
        ]
      },
      "properties": {
        "id": "xzo208901769",
        "user_id": "dqjwdx5rekzo",
        "title": "Lampara de pie",
        "description": "lampara de pie, 146cm de alto",
        "price": "10.0 EUR",
        "image": "https://cdn.wallapop.com/images/10420/h9/l1/__/c10420p1044022809/i5101516266.jpg?pictureSize=W320",
        "postal_code": "03690",
        "region": "Comunidad Valenciana"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -0.515289,
          38.399888
        ]
      },
      "properties": {
        "id": "9jdkvnwyy96k",
        "user_id": "9nz0oxdoeezo",
        "title": "Lamparas de techo ",
        "description": "2 Lamparas de techo",
        "price": "100.0 EUR",
        "image": "https://cdn.wallapop.com/images/10420/ha/o8/__/c10420p1045852312/i5113023268.jpg?pictureSize=W320",
        "postal_code": "03690",
        "region": "Comunidad Valenciana"
      }
    }
  ]
};

    // Añadir fuente GeoJSON al mapa
    map.on('load', function() {
        map.addSource('points', {
            "type": "geojson",
            "data": geojson
        });

        // Añadir una capa para mostrar los puntos
        map.addLayer({
            "id": "points",
            "type": "circle",
            "source": "points",
            "paint": {
                "circle-radius": 6,
                "circle-color": "#007cbf"
            }
        });

        // Crear popups cuando se hace clic en un punto
        map.on('click', 'points', function (e) {
            const coordinates = e.features[0].geometry.coordinates.slice();
            const properties = e.features[0].properties;

            // Contenido del popup incluyendo la imagen
            const popupContent = `
                <div class="popup-content">
                    <h3>${properties.title}</h3>
                    <p>${properties.description}</p>
                    <img src="${properties.image}" alt="Imagen" />
                </div>
            `;

            // Asegurarse de que el mapa se mueve con el zoom
            while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
                coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
            }

            // Crear el popup
            new maplibregl.Popup()
                .setLngLat(coordinates)
                .setHTML(popupContent)
                .addTo(map);
        });

        // Cambiar el cursor cuando pase por encima de un punto
        map.on('mouseenter', 'points', function () {
            map.getCanvas().style.cursor = 'pointer';
        });

        // Volver al cursor normal
        map.on('mouseleave', 'points', function () {
            map.getCanvas().style.cursor = '';
        });
    });
</script>

</body>
</html>
```



