from dataclasses import dataclass
from datetime import date, timedelta, time, datetime

@dataclass
class Workout:
    title: str
    date: date
    time: time
    distance: float
    duration: timedelta

    def __init__(self) -> None:
        self.title = "Untitled Workout"
        self.date = date.today()
        self.time = datetime.now()
        self.distance = 0.0
        self.duration = timedelta(0)


logbook = []
w1 = Workout()
w1.title = "Workout 1"
logbook.append(w1)
w2 = Workout()
w2.date = w2.date.replace(day=w2.date.day+1)
logbook.append(w2)
print(logbook)

workouts = [x for x in logbook if x.date == date.today()]
print(workouts)