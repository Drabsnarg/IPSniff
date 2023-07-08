#ip range to csv
import csv

ranges = [
    ('64.233.160.0', '64.233.191.255'),
    ('66.102.0.0', '66.102.15.255'),
    ('66.249.64.0', '66.249.95.255'),
    ('72.14.192.0', '72.14.255.255'),
    ('74.125.0.0', '74.125.255.255'),
    ('209.85.128.0', '209.85.255.255'),
    ('216.239.32.0', '216.239.63.255'),
    ('64.18.0.0', '64.18.15.255'),
    ('108.177.8.0', '108.177.15.255'),
    ('172.217.0.0', '172.217.31.255'),
    ('173.194.0.0', '173.194.255.255'),
    ('207.126.144.0', '207.126.159.255'),
    ('216.58.192.0', '216.58.223.255')
]

def generate_ip_addresses(start_ip, end_ip):
    start = list(map(int, start_ip.split('.')))
    end = list(map(int, end_ip.split('.')))
    
    ip_addresses = []
    while start <= end:
        ip_addresses.append('.'.join(map(str, start)))
        start[3] += 1
        for i in (3, 2, 1):
            if start[i] == 256:
                start[i] = 0
                start[i-1] += 1
    
    return ip_addresses

def write_ip_addresses_to_csv(ip_addresses, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['IP Address'])
        writer.writerows(zip(ip_addresses))

all_ip_addresses = []
for start, end in ranges:
    ip_addresses = generate_ip_addresses(start, end)
    all_ip_addresses.extend(ip_addresses)

write_ip_addresses_to_csv(all_ip_addresses, 'all_google_ip_addresses.csv')
print('CSV file all_google_ip_addresses.csv created successfully.')
