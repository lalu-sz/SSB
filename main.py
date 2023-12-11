# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import folium

# Using an HTML divider to create title
title = 'Where I Live, Breathe, and Died'
subtitle = 'Sexuality, Substance, and Becoming'
# title font: Palatino
# subtitle/para: Optima Nova
title_html = f'<h1 style="position:absolute;' \
             f'z-index:100000;' \
             f'left:50px;' \
             f'font-size:64px;' \
             f'font-family:Times New Roman;' \
             f'color:White" >{title}</h1>'

subtitle_html = f'<h3 style="position:absolute;' \
                f'z-index:100000;' \
                f'left:20px;' \
                f'top:80px;' \
                f'font-size:32px;' \
                f'font-family:Calibri;' \
                f'color:Gray" >{subtitle}</h3>'

begin = "the first breath. my first taste."
begin_html = f'<h3 style="position:absolute;' \
                f'z-index:100000;' \
                f'left:0px;' \
                f'top:690px;' \
                f'font-size:32px;' \
                f'font-family:Times New Roman;' \
                f'color:white" >{begin}</h3>'

m = folium.Map(location= (33.7626,-84.3750),
               min_zoom= 10,
               zoom_start=15,
               tiles="CartoDB.DarkMatter")
# Preview maptiles here: https://leaflet-extras.github.io/leaflet-providers/preview/
#default crs: EPSG3857 (projected; spherical mercator)

m.get_root().html.add_child(folium.Element(title_html))
m.get_root().html.add_child(folium.Element(subtitle_html))
m.get_root().html.add_child(folium.Element(begin_html))

#adding begin and end points (as buttons?)
m.get_root().html.add_child(folium.Element("""
<div style="position: fixed; 
     top: 0px; left: 1460px; width: 15px; height: 7px; 
    background-color:black; 
    border:none;
    z-index: 900;"> 
    <a href = "end.html">
        <button style = "font-size:32px;
        background-color:black;
         color:white;
         font-family:Times New Roman"
        >End</button>
    </a>
</div>
"""))



#add data
# save GEOJSON as WGS 84 (unprojected)
# https://stackoverflow.com/questions/59919104/geojson-layer-not-visible-on-python-folium-map
events = r'C:\Users\spark\OneDrive\Documents\DataScience_Projects\GEO600Final_WM\SSB_Places_CRS3857_CompletePOLY1.geojson'
# size is stored by GEOJSON; must stylize color scheme
dark2 = '#1C4557'
dark1 = '#5C7C8A'
neutral = '#969492'
light1 = '#B6976E'
light2 = '#FAD955'

def map_color(feature):
    if feature['properties']['Feeling_Assignment'] == -2:
        return dark2
    elif feature['properties']['Feeling_Assignment'] == -1:
        return dark1
    elif feature['properties']['Feeling_Assignment'] == 0:
        return neutral
    elif feature['properties']['Feeling_Assignment'] == 1:
        return light1
    elif feature['properties']['Feeling_Assignment'] == 2:
        return light2

folium.GeoJson(events,
               control=True,
               tooltip=folium.GeoJsonTooltip(fields=['Memory'],
                                             aliases=['memory:']),
               style_function=lambda feature: {
                   'fillColor': map_color(feature),
                   'fillOpacity':0.5,
                   'weight': 0
               }
               ).add_to(m)

#generate map
m.save("footprint.html")