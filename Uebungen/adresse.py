import requests

adresse = input("Adresse eingeben: ")

service = "https://api3.geo.admin.ch/rest/services/ech/SearchServer"

parameter = {"searchText": adresse,
             "type": "locations",
             "sr": 2056}

response = requests.get(url=service, params=parameter, verify=False)
result = response.json()

if len(result["results"]) > 0:
    treffer = result["results"][0]["attrs"]
    print("Ort:", treffer["detail"])
    print("Ost:", treffer["x"])
    print("Nord:", treffer["y"])
else:
    print("Keine Adresse gefunden.")
    
    
    