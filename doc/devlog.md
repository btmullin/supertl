## 2023-01-16

- Created GitHub repo
- Installed Python 3.11 on development machine
- Fixed use of gitbash and python per [this](https://stackoverflow.com/questions/32597209/python-not-working-in-the-command-line-of-git-bash)
- Installed pyenv
  - Realized I wanted venv not pyenv
- Created my virtual environment
- pip install pyside6
- Created base application from the example Qt

## 2023-01-17

- Want to figure out how to structure an application in Python and Qt
  - How to separate the view and the model
  - How to ensure the view gets updated when the model does
  - How to keep the view clean and structured for modularity and extensibility
- Anticipated UI components
  - Custom workout calendar widget
  - Weekly view
  - Workout overall panel
    - Workout map
    - Workout summary
    - Detailed graphs
  - World workout map
- Anticipated logbook model
  - Workout
    - Date
    - Time
    - Source file
    - Location
    - Duration
    - Distance
    - Summary info (averages)
    - Splits info
      - Saved with workout
      - Custom edited in app
- How to do data models in python?
  - Some type of dictionary
  - Is there a way to define the data items clearly
  - How to make it easy to persist and readback
  - Private versus public attributes

## 2023-01-19

- Looking up ways to read data files and store them
- https://pypi.org/project/fit-tool/
- https://pypi.org/project/openant/
- https://www.influxdata.com/products/influxdb/
- https://www.couchbase.com/resources/why-nosql

## 2023-01-21

- Looking over the logbook3 format
  - xml
  - Activities have track data in them with a version and CDATA
  - Unknown what the format is
  - Activity
    - fields
      - referenceId
      - startTime
      - timeZoneUtcOffset
      - hasStartTime
      - totalTime
      - totalDistance
      - notes
      - name
      - categoryName
      - userEnteredData
    - Laps
    - ExtensionData
      - Plugins
    - CustomData
    - GPSRoute
      - TrackData
    - DistanceTrack
      - TrackData
    - TimerPause
      - Pause
        - start
        - duration
- Playing with fit-tool
  - pip install fit_tool
  - pip install matplotlib
  - pip install numpy
    - Was already installed
  - FitFile.from_file is barfing on a ski and a run...
  - Try garmin-fit-sdk
    - pip install garmin-fit-sdk


### 2023-01-22

- Thinking about plotting
  - https://sites.northwestern.edu/researchcomputing/2022/02/03/what-is-the-best-interactive-plotting-package-in-python/
  - Good zooming on charts here
    - https://dash.gallery/ddk-operation-simulator/