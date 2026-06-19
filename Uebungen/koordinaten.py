import requests
import math


e_wgs = 7.452                                                                            # swisstopo Gebäude in WGS84
n_wgs = 46.928


service = "https://geodesy.geo.admin.ch/reframe/wgs84tolv95"                              # WGS84 → LV95 umrechnen

parameter = {"easting": e_wgs,                                                            # Baut die URL
             "northing": n_wgs,
             "format": "json"}

response = requests.get(url=service, params=parameter, verify=False)                      # Schickt die Anfrage
result = response.json()

e_swisstopo = float(result["easting"])
n_swisstopo = float(result["northing"])

print(f"swisstopo LV95: E {e_swisstopo:.0f} / N {n_swisstopo:.0f}")


e_schule = 2599716                                                                       # Schulungsgebäude bereits in LV95
n_schule = 1198800



distanz = math.sqrt((e_schule - e_swisstopo)**2 + (n_schule - n_swisstopo)**2)          #Pythagoras
distanz = round(distanz, -1)

print(f"Luftlinie: {distanz:.0f} m")