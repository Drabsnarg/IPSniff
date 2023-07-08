import requests
import folium

# Replace 'YOUR_API_KEY' with your actual API key from IPStack
IPSTACK_API_KEY = '3d24ba36982815e93e26fa0f1832bb1c'

def get_geolocation_data(ip_address):
    response = requests.get(f"http://api.ipstack.com/{ip_address}?access_key={IPSTACK_API_KEY}")
    data = response.json()
    return ip_address, data['latitude'], data['longitude']

def plot_on_map(locations):
    # Create a map centered on the first location
    geo_map = folium.Map(location=[locations[0][1], locations[0][2]])

    for ip, latitude, longitude in locations:
        folium.Marker([latitude, longitude], tooltip=f"IP: {ip}\nLat: {latitude}\nLon: {longitude}").add_to(geo_map)
    return geo_map

def main():
    ip_addresses = input("Enter IP addresses (separated by commas): ").split(',')
    locations = [get_geolocation_data(ip_address.strip()) for ip_address in ip_addresses]
    geo_map = plot_on_map(locations)
    geo_map.save('map.html')
    print("Map saved as map.html")

if __name__ == "__main__":
    main()
