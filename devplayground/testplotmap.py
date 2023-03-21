import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import folium
import webbrowser
import os

from garmin_fit_sdk import Decoder, Stream

stream = Stream.from_file("testdata/Woodland_20k.fit")
#stream = Stream.from_file("testdata/Snowy_Trail_Run.fit")
decoder = Decoder(stream)
messages, errors = decoder.read()

timestamp1 = []
hr1 = []
alt1 = []
speed1 = []
lat1 = []
lon1 = []

for rec in messages["record_mesgs"]:
    timestamp1.append(rec["timestamp"].timestamp())
    hr1.append(rec["heart_rate"])
    alt1.append(rec["enhanced_altitude"])
    speed1.append(rec["enhanced_speed"])
    lat1.append(rec["position_lat"]*180/2**31)
    lon1.append(rec["position_long"]*180/2**31)

start_timestamp = timestamp1[0]
time1 = np.array(timestamp1)
hr1 = np.array(hr1)
speed1 = np.array(speed1)
alt1 = np.array(alt1)
time1 = (time1 - start_timestamp)  # seconds
lat1 = np.array(lat1)
lon1 = np.array(lon1)

m = folium.Map()
points = list(zip(lat1,lon1))

# plot every 3rd point
#for p in points[::3]:
#    folium.Circle(radius = 3, location=p).add_to(m)

# Add start and end markers
folium.Marker(points[0], icon=folium.Icon(color="green", icon="circle-play", prefix="fa")).add_to(m)
folium.Marker(points[-1], icon=folium.Icon(color="red", icon="circle-stop", prefix="fa")).add_to(m)

# plot all lines
folium.PolyLine(points, weight=4, opacity=1).add_to(m)

sw = [lat1.min(), lon1.min()]
ne = [lat1.max(), lon1.max()]
m.fit_bounds([sw,ne])

mapfilename = os.path.join(os.getcwd(),'map.html')
m.save(mapfilename)
webbrowser.open(mapfilename)