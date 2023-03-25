import folium
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWebEngineWidgets import QWebEngineView
from supertl.Data import Activity
import io

class ActivityMapWidget(QWebEngineView):
    def __init__(self):
        super().__init__()

        self.setHtml('<H1>Nothing Yet</H1>')
        #f = open('c:/git/supertl/devplayground/map.html','r')
        #self.setHtml(f.read())

    def set_activity(self, activity: Activity):
        points = list(zip(activity.gps_data.time_series_data['position_lat'],
                          activity.gps_data.time_series_data['position_long']))

        map = folium.Map()

        # Add start and end markers
        folium.Marker(points[0],
                      icon=folium.Icon(color="green", icon="circle-play", prefix="fa")).add_to(map)
        folium.Marker(points[-1],
                      icon=folium.Icon(color="red", icon="circle-stop", prefix="fa")).add_to(map)

        # plot all lines
        folium.PolyLine(points, weight=4, opacity=1).add_to(map)

        # zoom to the activity
        sw = [activity.gps_data.time_series_data['position_lat'].min(),
              activity.gps_data.time_series_data['position_long'].min()]
        ne = [activity.gps_data.time_series_data['position_lat'].max(),
              activity.gps_data.time_series_data['position_long'].max()]
        map.fit_bounds([sw,ne])

        # update the map
        data = io.BytesIO()
        map.save(data, close_file=False)
        self.setHtml(data.getvalue().decode())
