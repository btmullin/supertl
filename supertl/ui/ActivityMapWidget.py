import folium
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWebEngineWidgets import QWebEngineView
from supertl.Data import Activity
import io

class ActivityMapWidget(QtWidgets.QFrame):
    """
    A widget that will visually display the gps route of an activity.

    Args:
        QWebEngineView (_type_): _description_
    """

    def __init__(self, parent):
        super().__init__(parent)

        self.layout = QtWidgets.QGridLayout(self)

        self.webengine = QWebEngineView()
        self.webengine.setHtml('<H1 style="padding:100px;"><CENTER>No Activity Selected</CENTER></H1>')

        self.label = QtWidgets.QLabel('Test Label', alignment=QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("max-height: 20px;")

        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.webengine, 1, 0)

    def set_activity(self, activity: Activity):
        """
        Set the activity to be displayed by the Activity Map and redraw the map.

        Args:
            activity (Activity): The Activity to display.
        """
        points = list(zip(activity.gps_data.time_series_data['position_lat'],
                          activity.gps_data.time_series_data['position_long']))

        f_map = folium.Map()

        # Add start and end markers
        folium.Marker(points[0],
                      icon=folium.Icon(color="green",
                                       icon="circle-play",
                                       prefix="fa")).add_to(f_map)
        folium.Marker(points[-1],
                      icon=folium.Icon(color="red", icon="circle-stop", prefix="fa")).add_to(f_map)

        # plot all lines
        folium.PolyLine(points, weight=4, opacity=1).add_to(f_map)

        # zoom to the activity
        sw_limit = [activity.gps_data.time_series_data['position_lat'].min(),
                    activity.gps_data.time_series_data['position_long'].min()]
        ne_limit = [activity.gps_data.time_series_data['position_lat'].max(),
                    activity.gps_data.time_series_data['position_long'].max()]
        f_map.fit_bounds([sw_limit, ne_limit])

        # update the map
        data = io.BytesIO()
        f_map.save(data, close_file=False)
        self.webengine.setHtml(data.getvalue().decode())
