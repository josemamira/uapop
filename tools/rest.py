import requests

api_url = "https://api.wallapop.com/api/v3/search"
params = {
    "source":"quick_filters",
    "keywords": "monitor",
    "latitude": "38.3827",
    "longitude": "-0.5113",
    "order_by":"closest",
    "distance_in_km":1
}

data = requests.get(api_url, params=params).json()
# cabecera
print(
    "{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
        "title",
        "price",  
        "image",             
        "category_id",                        
        "url",
        "description"            
    )
)
# datos
for o in data["data"]["section"]["payload"]["items"]:
    print(
        "{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
            o["title"],
            o["price"]["amount"],  
            o["images"][0]["urls"]["small"],             
            o["category_id"],                        
            "https://es.wallapop.com/item/" + o["web_slug"],
            o["description"]            
        )
    )
