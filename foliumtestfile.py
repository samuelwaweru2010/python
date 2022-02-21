import folium

m = folium.Map(location=[1.1018, 37.0144], zoom_start=12)
#m = folium.Map(location=[42.3601, -71.0589], zoom_start=12)
tooltip ='Click for More'

folium.Marker([-1.1066294, 37.01523],
              popup='<strong>On Location</trong>',
              tooltip=tooltip).add_to(m)
folium.Marker([-1.1000, 37.0135],
              popup='<strong>On Loc dude</trong>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m)

folium.Marker([-1.990, 37.0130],
              popup='<strong>On Loc dude</trong>',
              tooltip=tooltip,
              icon=folium.Icon(color='pink')).add_to(m)
folium.Marker([-1.988, 37.0128],
              popup='<strong>On Loc dude</trong>',
              tooltip=tooltip,
              icon=folium.Icon(color='green', icon='leaf')).add_to(m)

m.save('map.html')