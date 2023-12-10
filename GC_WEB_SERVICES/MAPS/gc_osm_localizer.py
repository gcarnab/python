import requests
import folium
from folium import plugins
import pandas as pandas

# https://www.youtube.com/watch?v=TDlo7s4SZA8&list=PL-2EBeDYMIbRppDpfO5osdSeUFIOuZz-2&index=2

data_base_path = "GC_WEB_SERVICES/MAPS/DATA/"
data_base_absolute_path = "C:/DEV/workspace/vscode/python/GC_WEB_SERVICES/MAPS/DATA/"

def geocode(address):
    endpoint = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': address,
        'format': 'json'
    }
    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        if len(data) > 0:
            location = data[0]
            lat, lon = location['lat'], location['lon']
            print(f"Geocoded coordinates for '{address}': {lat}, {lon}")
            return lat, lon
        else:
            print(f"No results found for '{address}'")
    else:
        print(f"Error in geocoding request. Status code: {response.status_code}")

def reverse_geocode(lat, lon):
    endpoint = "https://nominatim.openstreetmap.org/reverse"
    params = {
        'lat': lat,
        'lon': lon,
        'format': 'json'
    }
    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        address = data.get('display_name', 'Address not found')
        print(f"Reverse geocoded address for coordinates ({lat}, {lon}): {address}")
        return address
    else:
        print(f"Error in reverse geocoding request. Status code: {response.status_code}")

def plot_map(lat, lon, address, tile_layer='OpenStreetMap', satellite=False):
    # Create a folium map centered at the specified coordinates
    map_center = [lat, lon]
    #my_map = folium.Map(location=map_center, zoom_start=16, control_scale=True)
    my_map = folium.Map(location=map_center, zoom_start=16)
    
    # Add a marker for the specified coordinates
    folium.Marker(location=map_center , 
                  icon=folium.Icon(icon='info-sign'),
                  popup=address).add_to(my_map)

    # Add a legend
    folium.LayerControl().add_to(my_map)

    # Add a legend
    #legend_html = '<img src="C:/DEV/workspace/vscode/python/GC_WEB_SERVICES/MAPS/DATA/map.jpg" width="150" height="100">'
    #my_map.get_root().html.add_child(folium.Element(legend_html))

     # Add a satellite layer if specified
    if satellite:
        folium.TileLayer('Stamen Terrain', attr='Stamen Terrain').add_to(my_map)

    # Add the specified tile layer with attribution
    #folium.TileLayer(tile_layer, attr=f'{tile_layer} Attribution').add_to(my_map)

    # Save the map as an HTML file and open it in the default web browser
    map_filename = data_base_absolute_path + 'map.html'
    my_map.save(map_filename)
    print(f"Map plotted and saved as '{map_filename}'")
    folium.Map(location=map_center).save(map_filename)
    import webbrowser
    webbrowser.open(map_filename)

def main_menu():
    print("Scegli un'opzione:")
    print("1. Geocodifica un indirizzo")
    print("2. Reverse geocodifica coordinate")
    print("3. Visualizza la mappa")
    print("4. Visualizza la mappa (Satellite)")
    print("5. Pulisci la mappa")
    print("x. Uscire")

def main():
    while True:
        main_menu()
        choice = input("Inserisci il numero dell'opzione desiderata: ")

        if choice == '1':
            address = input("Inserisci l'indirizzo da geocodificare: ")
            lat, lon = geocode(address)
        elif choice == '2':
            lat = float(input("Inserisci la latitudine: "))
            lon = float(input("Inserisci la longitudine: "))
            reverse_geocode(lat, lon)
        elif choice == '3':
            if 'lat' in locals() and 'lon' in locals():
                address = reverse_geocode(lat, lon)
                plot_map(lat, lon, address)
            else:
                print("Devi prima eseguire la geocodifica o la reverse geocodifica.")
        elif choice == '4':
            if 'lat' in locals() and 'lon' in locals():
                address = reverse_geocode(lat, lon)
                plot_map(lat, lon, address, satellite=True)
            else:
                print("Devi prima eseguire la geocodifica o la reverse geocodifica.")
        elif choice == '5':
            if 'lat' in locals() and 'lon' in locals():
                folium.Map().save(data_base_path + 'map.html')
                print("Mappa pulita.")
            else:
                print("Nessuna mappa da pulire.")                
        elif choice == 'x' or choice == 'X' :
            print("Uscita.")
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()
