from cone_area_lib import cone_area

radius = float(input("Radius: "))
height = float(input("Höhe: "))

area = cone_area(radius, height)

print("Mantelfläche:", round(area, 2))
