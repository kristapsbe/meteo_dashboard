import pandas as pd

from settings import key
from datetime import datetime

coords = []

with open("server.log", "r") as f:
    while line := f.readline():
        if '/api/v1/forecast/cities?lat=' in line:
            coords.append([
                datetime.strptime(line.split(",")[0][1:], '%Y-%m-%d %H:%M:%S'), # time
                float(line.split("=")[1].split("&")[0]), # lat
                float(line.split("=")[2].split("&")[0].split(" ")[0]) # lon
            ])

df = pd.DataFrame(coords)
#print(df)
coordstr = ','.join([f"new google.maps.LatLng({c[1]}, {c[2]})" for c in coords])

with open("map.js", "w") as f:
    f.write("".join(open("map.temp.js", "r").readlines()).replace("<latlng>", coordstr))

with open("map.html", "w") as f:
    f.write("".join(open("map.temp.html", "r").readlines()).replace("<key>", key))
