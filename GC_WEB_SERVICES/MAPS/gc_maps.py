import plotly.express as px
import pandas as pd 

print("Getting data...")
data_base_path = "GC_WEB_SERVICES/MAPS/DATA/"

df = px.data.carshare()
print(df.head(10))
print(df.tail(10))

fig = px.scatter_mapbox(df,
                        lon=df['centroid_lon'], 
                        lat=df['centroid_lat'],
                        zoom=1, 
                        color=df['peak_hour'], 
                        size=df['car_hours'],
                        width=400,
                        height=300,
                        title="GC Map")
fig.update_layout(mapbox_style="open-stree-map")
fig.update_layout(margin={"r": 5, "l" : 5, "t": 5, "b" : 5 })
#fig.write_html(data_base_path + 'first_figure.html', auto_open=True)
fig.show()