import requests

# Replace 'YOUR_API_KEY' with your actual API key from IPStack
IPSTACK_API_KEY = '65456a7c52d3262bf1272de1dcbda0e9'

def get_geolocation_data(ip_address):
    response = requests.get(f"http://api.ipstack.com/{ip_address}?access_key={IPSTACK_API_KEY}")
    data = response.json()
    print(data)  # Print the API response for debugging purposes
    return data['latitude'], data['longitude']

def main():
    ip_addresses = input("Enter IP addresses (separated by commas): ").split(',')
    locations = [get_geolocation_data(ip_address.strip()) for ip_address in ip_addresses]
    print(locations)  # Print the extracted locations for debugging purposes

if __name__ == "__main__":
    main()
