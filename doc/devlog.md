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