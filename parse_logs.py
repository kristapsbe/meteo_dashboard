import pandas as pd

from settings import key
from datetime import datetime

coords = []
rounding = 2

with open("server.log", "r") as f:
    while line := f.readline():
        if '/api/v1/forecast/cities?lat=' in line:
            coords.append([
                str(round(float(line.split("=")[1].split("&")[0]), rounding)), # lat
                str(round(float(line.split("=")[2].split("&")[0].split(" ")[0]), rounding)), # lon
                #datetime.strptime(line.split(",")[0][1:], '%Y-%m-%d %H:%M:%S'), # time
            ])

unique_coords = [e.split(",") for e in list(set([",".join(c) for c in coords]))]
df = pd.DataFrame(unique_coords)
#print(df)
coordstr = ','.join([f"new google.maps.LatLng({c[0]}, {c[1]})" for c in unique_coords])

with open("map.js", "w") as f:
    f.write("".join(open("map.temp.js", "r").readlines()).replace("<latlng>", coordstr))

with open("map.html", "w") as f:
    f.write("".join(open("map.temp.html", "r").readlines()).replace("<key>", key))
