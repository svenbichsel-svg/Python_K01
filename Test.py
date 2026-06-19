import folium
import geopandas as gpd
import pandas as pd
import webbrowser

df = pd.read_csv("messpunkte.csv")
gdf_punkte = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df["ost"], df["nord"]), crs="EPSG:2056"
)

gdf_zonen = gpd.read_file("messgebiete.geojson")

if gdf_zonen.crs is None:
    gdf_zonen.crs = "EPSG:4326"
gdf_zonen_2056 = gdf_zonen.to_crs("EPSG:2056")

gdf_join = gpd.sjoin(gdf_punkte, gdf_zonen_2056, how="left", predicate="within")

punkte_ohne_zone = gdf_join[gdf_join["index_right"].isna()]

print("--- Punkte ohne Zonen-Zuordnung ---")
if not punkte_ohne_zone.empty:
    print(punkte_ohne_zone["name_left"], punkte_ohne_zone["hoehe"])
else:
    print("Alle Punkte konnten einer Zone zugeordnet werden.")
print("-----------------------------------\n")

gdf_punkte_wgs84 = gdf_punkte.to_crs("EPSG:4326")
gdf_zonen_wgs84 = gdf_zonen.to_crs("EPSG:4326")

mitte = gdf_punkte_wgs84.geometry.union_all().centroid

karte = folium.Map(
    location=[mitte.y, mitte.x],
    zoom_start=10,
    tiles="https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/{z}/{x}/{y}.jpeg",
    attr="swisstopo",
)

farben = ["red", "blue", "green", "purple", "orange", "darkred", "cadetblue"]


def style_funktion(feature):
    feature_id = feature.get("id", 0)
    if isinstance(feature_id, str) and feature_id.isdigit():
        idx = int(feature_id)
    else:
        idx = hash(str(feature_id))
    farbe = farben[idx % len(farben)]

    return {
        "fillColor": farbe,
        "color": farbe,
        "weight": 2,
        "fillOpacity": 0.4,
    }


folium.GeoJson(
    gdf_zonen_wgs84,
    style_function=style_funktion,
    tooltip=folium.GeoJsonTooltip(
        fields=["name"], aliases=["Zone:"]
    ),  
).add_to(karte)

for _, row in gdf_punkte_wgs84.iterrows():
    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        tooltip=f"{row['name']}: {row['hoehe']} m.ü.M.",
    ).add_to(karte)

karte.save("messpunkte.html")
webbrowser.open("messpunkte.html")

print("Karte gespeichert: messpunkte.html")