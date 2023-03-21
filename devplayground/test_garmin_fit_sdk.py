import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from garmin_fit_sdk import Decoder, Stream

stream = Stream.from_file("testdata/Woodland_20k.fit")
decoder = Decoder(stream)
messages, errors = decoder.read()

print("Errors: ", errors)
print()
print("Message Keys: ", messages.keys())
print()
print("File ID Messages: ", messages["file_id_mesgs"])
print()
print("Session Messages: ", messages["session_mesgs"])
print()
print("Laps")
i = 1
for lap in messages["lap_mesgs"]:
    print("Lap ", i, ": ", lap)
    print()
    i = i + 1
print("Events: ", messages["event_mesgs"])
print()
print("288: ", messages["288"])


for key in messages:
    print(key, ": ", len(messages[key]))


print(messages["record_mesgs"][0])

timestamp1 = []
hr1 = []
alt1 = []
speed1 = []

for rec in messages["record_mesgs"]:
    timestamp1.append(rec["timestamp"].timestamp())
    hr1.append(rec["heart_rate"])
    alt1.append(rec["enhanced_altitude"])
    speed1.append(rec["enhanced_speed"])

start_timestamp = timestamp1[0]
time1 = np.array(timestamp1)
hr1 = np.array(hr1)
speed1 = np.array(speed1)
alt1 = np.array(alt1)
time1 = (time1 - start_timestamp)  # seconds

#
# Plot the data
#
ax1 = plt.subplot(311)
ax1.plot(time1, hr1, 'r-o', label='app [bpm]')
ax1.legend(loc="upper right")
plt.xlabel('Time (s)')
plt.ylabel('HR (bpm)')

plt.subplot(312, sharex=ax1)
plt.plot(time1, speed1, '-o', label='app [m/s]')
plt.legend(loc="upper right")
plt.xlabel('Time (s)')
plt.ylabel('speed (m/s)')
    
plt.subplot(313, sharex=ax1)
plt.plot(time1, alt1, '-o', label='app [m]')
plt.legend(loc="upper right")
plt.xlabel('Time (s)')
plt.ylabel('alt (m)')

plt.show()
