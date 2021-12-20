import geocoder
import folium

g = geocoder.ip("49.36.173.35")

MyAddress = g.latlng
print(MyAddress)

MyMap = folium.Map(location=MyAddress, zoom_start=12)
folium.CircleMarker(location=MyAddress, radius=50, popup="Lucknow").add_to(MyMap)
folium.Marker(MyAddress, popup="Lucknow").add_to(MyMap)
MyMap.save("MyMap.html")