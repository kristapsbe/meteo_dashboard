import pandas as pd

from settings import key
from datetime import datetime

coords = []

with open("server.log", "r") as f:
    while line := f.readline():
        if '/api/v1/forecast/cities?lat=' in line:
            coords.append([
                str(float(line.split("=")[1].split("&")[0])), # lat
                str(float(line.split("=")[2].split("&")[0].split(" ")[0])), # lon
                #datetime.strptime(line.split(",")[0][1:], '%Y-%m-%d %H:%M:%S'), # time
            ])

df = pd.DataFrame([e.split(",") for e in list(set([",".join(c) for c in coords]))])
#print(df)
coordstr = ','.join([f"new google.maps.LatLng({c[0]}, {c[1]})" for c in coords])

with open("map.js", "w") as f:
    f.write("".join(open("map.temp.js", "r").readlines()).replace("<latlng>", coordstr))

with open("map.html", "w") as f:
    f.write("".join(open("map.temp.html", "r").readlines()).replace("<key>", key))
