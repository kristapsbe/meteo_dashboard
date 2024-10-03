from datetime import datetime

coords = []

with open("server.log", "r") as f:
    while line := f.readline():
        if '/api/v1/forecast/cities?lat=' in line:
            coords.append([
                datetime.strptime(line.split(",")[0][1:], '%Y-%m-%d %H:%M:%S'), # time
                float(line.split("=")[1].split("&")[0]), # lat
                float(line.split("=")[2].split("&")[0]) # lon
            ])

print(coords)
