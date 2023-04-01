import pandas as pd
import folium

# read dataset into a dataframe
df = pd.read_csv('GrowLocations.csv')

# remove bad values
df = df[(df['Longitude'] >= -10.592) & (df['Longitude'] <= 1.6848) &
        (df['Latitude'] >= 50.681) & (df['Latitude'] <= 57.985)]

# create a map object centered on the UK
map_obj = folium.Map(location=[53.508, -2.476], zoom_start=6)

# add a marker for each sensor location
for index, row in df.iterrows():
    folium.Marker(location=[row['Latitude'], row['Longitude']]).add_to(map_obj)

# display the map
map_obj.show_in_browser()