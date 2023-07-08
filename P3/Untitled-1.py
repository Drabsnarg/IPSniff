import os
import requests
import json
import shutil

# Replace with your actual values
ACCESS_TOKEN = 'eyJ0eXAiOiJKV1QiLCJub25jZSI6IlYyWlMxS2V4UXpIODVHXzV0ZjJVMkIyN2xGaGkxNHVyN1dmSk1YREpTVEUiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9iMzkwZWU5My1iYjMxLTQ5ZTQtOWI4ZC0wMDA2MTFiZDQ2OWQvIiwiaWF0IjoxNjgzMjE2MTgwLCJuYmYiOjE2ODMyMTYxODAsImV4cCI6MTY4MzIyMDA4MCwiYWlvIjoiRTJaZ1lEalc2aDR1dTlkNWJrMzhET1c2K2JIM0FBPT0iLCJhcHBfZGlzcGxheW5hbWUiOiJPbmUgZHJpdmUgMSIsImFwcGlkIjoiMjAzOTZmNDgtOGMxOS00NWIxLTk0NDItZThiMTg3ZTAxMDNkIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvYjM5MGVlOTMtYmIzMS00OWU0LTliOGQtMDAwNjExYmQ0NjlkLyIsImlkdHlwIjoiYXBwIiwib2lkIjoiYjUyMTQ0MDUtMTZmOS00MGJhLWFhZDEtYzc1OWEzYjg5NzYyIiwicmgiOiIwLkFWSUFrLTZRc3pHNzVFbWJqUUFHRWIxR25RTUFBQUFBQUFBQXdBQUFBQUFBQUFDNkFBQS4iLCJzdWIiOiJiNTIxNDQwNS0xNmY5LTQwYmEtYWFkMS1jNzU5YTNiODk3NjIiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiTkEiLCJ0aWQiOiJiMzkwZWU5My1iYjMxLTQ5ZTQtOWI4ZC0wMDA2MTFiZDQ2OWQiLCJ1dGkiOiJJZ3pGMTFBYktFLXh6bk5HenRrRUFRIiwidmVyIjoiMS4wIiwid2lkcyI6WyIwOTk3YTFkMC0wZDFkLTRhY2ItYjQwOC1kNWNhNzMxMjFlOTAiXSwieG1zX3RjZHQiOjE2NzQxODQwNjN9.mLwVlkB_C6tD4tIu7cOo7vQKCZHhvy-umw7JCIy-7L6uWFwymNEzJchFmpZBc0tbv3gR-DCnWBOSF46eJUnORX-Qjac2blONwC_wJj-McSoq_Nx1YO-gkLsW28a052JoYcMwAxNcN2fs9iJ-7WGoTpLkkyBQqCVoTg9JszsLYO-6Usfj8mCNKxpvtaikSlBthY2XSOiXAl_dN9xb9qx6mOB0QOhHnvHav8SiG9wDIOGBdKBD3DcQBAR3PPbPZn5TlO-tS7NqH6-itWpRIdry6e0EQxNNHNB2s6NP0UPy8gBTmn7VHDwEeoJiV23SpLw7b0jnbaX2UTt2uHtW4xTSaw'
PHOTO_FOLDER_NAME = 'Evony'

# Set up headers for the API requests
headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}

# Get the root folder of your OneDrive
drive_response = requests.get('https://graph.microsoft.com/v1.0/me/drive/root', headers=headers)
drive_response_data = json.loads(drive_response.text)
drive_id = drive_response_data['id']

# Search for all photos with "evony" in their name in your OneDrive
query = "evony"
search_response = requests.get(f"https://graph.microsoft.com/v1.0/me/drive/root/search(q='{query}')", headers=headers)
search_response_data = json.loads(search_response.text)

# Create a new folder on your desktop to store the photos
desktop_path = os.path.expanduser("~/Desktop")
new_folder_path = os.path.join(desktop_path, PHOTO_FOLDER_NAME)
os.makedirs(new_folder_path, exist_ok=True)

# Loop through the search results and move the photos to the new folder on your desktop
for item in search_response_data['value']:
    item_id = item['id']
    item_name = item['name']
    item_download_url = item['@microsoft.graph.downloadUrl']
    item_path = os.path.join(new_folder_path, item_name)
    with requests.get(item_download_url, headers=headers, stream=True) as r:
        with open(item_path, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    # Delete the original file from OneDrive
    delete_response = requests.delete(f"https://graph.microsoft.com/v1.0/me/drive/items/{item_id}", headers=headers)

print("Done!")
