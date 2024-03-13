# cone_area_app.py

# Importieren der Funktion cone_area aus der Datei cone_area_lib.py
from exercises_from_proglang.solutions_chatgpt_4_0.sheet_03.ex_3_1a import cone_area # this was added manually, not by chatgpt, to fit the data structure

# Einlesen der Werte für Radius und Höhe vom Benutzer
radius = float(input("Radius: "))
height = float(input("Höhe: "))

# Berechnen der Mantelfläche des Kegels
mantelflaeche = cone_area(radius, height)

# Ausgabe der berechneten Mantelfläche
print(f"Mantelfläche: {mantelflaeche:.2f}")
