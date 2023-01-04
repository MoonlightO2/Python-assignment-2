# import folium
# from folium.plugins import minimap
import numpy as np
import pandas as pd
import webbrowser
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import gc

start = time.process_time()

# Load data from CSV to Dataset "data"
data = pd.read_csv('GrowLocations.csv')
print("\nGrow Locations Dataset - Shape (Before cleaning)")
print(data.shape)

# Displaying the list of column names
print('\nList of column names : ', list(data.columns))

# Removing erroneous data
print("\nShow all erroneous data....")
print(data.isna().sum())
print("\nRemoving erroneous data....")
data = data.dropna(subset=['Serial'])
print("\nErroneous data removed....")
print("\nGrow Locations Dataset - First 5 rows")
print(data.head())
print("\nGrow Locations Dataset - Shape (After cleaning)")
print(data.shape)
print("\nGrow Locations Dataset - Data Types")
print(data.dtypes)

# Print dataset into CSV - export to csv to see whether the dataset has all clean data
print("\nExport dataset into CSV - File created - GrowLocations-Cleaned.csv...")
data.to_csv('GrowLocations-Cleaned.csv', index=False)

print("\nShow all unique types")
data = pd.DataFrame(data)
data.Type = data.Type.replace('Thingful.Connectors.GROWSensors.AirTemperature', 'Air Temperature')
data.Type = data.Type.replace('Thingful.Connectors.GROWSensors.BatteryLevel', 'Battery Level')
data.Type = data.Type.replace('Thingful.Connectors.GROWSensors.FertilizerLevel', 'Fertilizer Level')
data.Type = data.Type.replace('Thingful.Connectors.GROWSensors.Light', 'Light')
data.Type = data.Type.replace('Thingful.Connectors.GROWSensors.SoilMoisture', 'Soil Moisture')
data.Type = data.Type.replace('Thingful.Connectors.GROWSensors.WaterTankLevel', 'Water Tank Level')

# print(data.Type.unique())
print("\nTypes list")
print(data['Type'].value_counts())

# find max/min, plug into a website, snip area as png and insert as plotmap
BBox = ((-10.592, 1.6848, 50.681, 57.985))

# read the image in, plot points over image
grow_map = "map7.png"
truth_plot = plt.imread(grow_map)
fig, ax = plt.subplots(figsize=(8, 8), linewidth=0.1)
plot_title = "Grow Locations UK"
ax.set_title(plot_title)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_xlim(BBox[0], BBox[1])
ax.set_ylim(BBox[2], BBox[3])

scat = ax.scatter(data.Latitude, data.Longitude, zorder=1, alpha=0.5, c='b', s=10)
color_data = np.random.random((500, len(data.Latitude)))


def update(frame):
    scat.set_array(color_data[frame])
    return scat,


anime = FuncAnimation(fig, update, frames=range(500), blit=True)

ax.imshow(truth_plot, zorder=0, extent=BBox, aspect='equal')
print("\nLoading map image....")
print("\nTime taken to load map image....", time.process_time() - start)
plt.show()
print("\nMap image closed....")

print("\n\nTotal time taken: ", time.process_time() - start)

print("\nDeleting data to clear memory....")
del data
gc.collect()
try:
    print(data)
except:
    print("\nMemory cleared successfully....")
