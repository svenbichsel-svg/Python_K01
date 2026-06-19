import os
import pandas as pd
import geopandas as gpd
import folium

# Ordner, in dem dieses Skript liegt
skript_ordner = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(os.path.join(skript_ordner, "messpunkte.csv"))

gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df["ost"], df["nord"]),
    crs="EPSG:2056"
)

zonen = gpd.read_file(os.path.join(skript_ordner, "messgebiete.geojson"))            # Messgebiete laden


gdf_wgs84 = gdf.to_crs("EPSG:4326")                                                 # Nach WGS84 umprojizieren
zonen_wgs84 = zonen.to_crs("EPSG:4326")


joined = gpd.sjoin(gdf_wgs84, zonen_wgs84, how="left", predicate="within")          # Räumlicher Join 
print(joined.columns.tolist())

ohne_zone = joined[joined["index_right"].isna()]                                    # Punkte ohne Zone
if ohne_zone.empty:
    print("Alle Punkte liegen in einer Zone.")
else:
    print("Punkte ohne Zone:")
    print(ohne_zone[["name_left", "hoehe"]])


print("\nPunkte mit Zone:")                                                         # Punkte mit Zone
print(joined[["name_left", "hoehe", "code"]].to_string(index=False))    


mitte = gdf_wgs84.geometry.union_all().centroid                                     # Karte erstellen

karte = folium.Map(
    location=[mitte.y, mitte.x],
    zoom_start=10,
    tiles="https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/{z}/{x}/{y}.jpeg",
    attr="swisstopo",
)

farben = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00"]

folium.GeoJson(
    zonen_wgs84,
    name="Zonen",
    style_function=lambda feature, farben=farben: {
        "fillColor": farben[int(feature["id"]) % len(farben)],
        "color": "black",
        "weight": 1,
        "fillOpacity": 0.4,
    },
    tooltip=folium.GeoJsonTooltip(fields=["code"], aliases=["Zone:"])
).add_to(karte)

for _, row in joined.iterrows():                                                   # Messpunkte als Marker
    zone_text = row["code"] if pd.notna(row["code"]) else "keine Zone"
    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        tooltip=f"{row['name_left']}: {row['hoehe']} m.ü.M. | Zone: {zone_text}"
    ).add_to(karte)

karte.save(os.path.join(skript_ordner, "messpunkte_zonen.html"))