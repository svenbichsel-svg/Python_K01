import pandas as pd
import geopandas as gpd
import folium


df = pd.read_csv("messpunkte.csv")                                      # messpunkte.csv einlesen 


gdf = gpd.GeoDataFrame(                                                 # DataFrame in GeoDataFrame umwandeln
    df,
    geometry=gpd.points_from_xy(df["ost"], df["nord"]),
    crs="EPSG:2056"  # LV95
)


gdf_wgs84 = gdf.to_crs("EPSG:4326")                                      # Nach WGS84 umprojizieren


mitte = gdf_wgs84.geometry.union_all().centroid                          # Kartenmittelpunkt


karte = folium.Map(                                                     # Korrdinaten eigeben
    location=[mitte.y, mitte.x],
    zoom_start=10,
    tiles="https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/{z}/{x}/{y}.jpeg",
    attr="swisstopo",
)


for _, row in gdf_wgs84.iterrows():                                     # Alle Messungen als Marker hinzufügen
    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        tooltip=f"{row['name']}: {row['hoehe']} m.ü.M."
    ).add_to(karte)


karte.save("messpunkte.html")