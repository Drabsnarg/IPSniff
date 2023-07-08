import requests

# Replace with your actual values
TENANT_ID = 'b390ee93-bb31-49e4-9b8d-000611bd469d'
CLIENT_ID = '20396f48-8c19-45b1-9442-e8b187e0103d'
CLIENT_SECRET = 'x6r8Q~5tTiQbUpI5qswepB0EQcy9EO0-EKhQBc5R'

# Set up the token endpoint and parameters
token_endpoint = f'https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token'
params = {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'scope': 'https://graph.microsoft.com/.default'
}

# Send a POST request to the token endpoint to get an access token
response = requests.post(token_endpoint, data=params)
response_data = response.json()
access_token = response_data['access_token']

print(access_token)
