import csv
import requests
import folium
import os
from concurrent.futures import ThreadPoolExecutor

IPSTACK_API_KEY = '65456a7c52d3262bf1272de1dcbda0e9'
MAX_WORKERS = 10

def get_geolocation_data(ip_address):
    response = requests.get(f"http://api.ipstack.com/{ip_address}?access_key={IPSTACK_API_KEY}")
    data = response.json()
    try:
        latitude = data['latitude']
        longitude = data['longitude']
    except KeyError:
        latitude = None
        longitude = None
    return ip_address, latitude, longitude

def plot_on_map(locations):
    geo_map = folium.Map(location=[locations[0][1], locations[0][2]])

    for ip, latitude, longitude in locations:
        folium.Marker([latitude, longitude], tooltip=f"IP: {ip}\nLat: {latitude}\nLon: {longitude}").add_to(geo_map)
    return geo_map

def read_ip_addresses_from_csv(filename):
    ip_addresses = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            ip_addresses.extend(row)
    return ip_addresses

def main():
    csv_filename = input("Enter the CSV file name (without .csv extension): ")
    csv_filename += ".csv"
    output_name = os.path.splitext(csv_filename)[0]
    ip_addresses = read_ip_addresses_from_csv(csv_filename)
    
    # Create a ThreadPoolExecutor with a specified number of workers
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Submit geolocation requests for each IP address using the executor
        futures = [executor.submit(get_geolocation_data, ip_address.strip()) for ip_address in ip_addresses if ip_address.strip()]
        
        # Wait for all futures to complete and retrieve the results
        locations = [future.result() for future in futures if future.result()[1] and future.result()[2]]
    
    geo_map = plot_on_map(locations)
    filename = f"{output_name}_map.html"
    geo_map.save(filename)
    print(f"Map saved as {filename}")

if __name__ == "__main__":
    main()
 