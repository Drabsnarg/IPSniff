import os
import requests

# Set the access token
access_token = "eyJ0eXAiOiJKV1QiLCJub25jZSI6IlYyWlMxS2V4UXpIODVHXzV0ZjJVMkIyN2xGaGkxNHVyN1dmSk1YREpTVEUiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9iMzkwZWU5My1iYjMxLTQ5ZTQtOWI4ZC0wMDA2MTFiZDQ2OWQvIiwiaWF0IjoxNjgzMjE2MTgwLCJuYmYiOjE2ODMyMTYxODAsImV4cCI6MTY4MzIyMDA4MCwiYWlvIjoiRTJaZ1lEalc2aDR1dTlkNWJrMzhET1c2K2JIM0FBPT0iLCJhcHBfZGlzcGxheW5hbWUiOiJPbmUgZHJpdmUgMSIsImFwcGlkIjoiMjAzOTZmNDgtOGMxOS00NWIxLTk0NDItZThiMTg3ZTAxMDNkIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvYjM5MGVlOTMtYmIzMS00OWU0LTliOGQtMDAwNjExYmQ0NjlkLyIsImlkdHlwIjoiYXBwIiwib2lkIjoiYjUyMTQ0MDUtMTZmOS00MGJhLWFhZDEtYzc1OWEzYjg5NzYyIiwicmgiOiIwLkFWSUFrLTZRc3pHNzVFbWJqUUFHRWIxR25RTUFBQUFBQUFBQXdBQUFBQUFBQUFDNkFBQS4iLCJzdWIiOiJiNTIxNDQwNS0xNmY5LTQwYmEtYWFkMS1jNzU5YTNiODk3NjIiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiTkEiLCJ0aWQiOiJiMzkwZWU5My1iYjMxLTQ5ZTQtOWI4ZC0wMDA2MTFiZDQ2OWQiLCJ1dGkiOiJJZ3pGMTFBYktFLXh6bk5HenRrRUFRIiwidmVyIjoiMS4wIiwid2lkcyI6WyIwOTk3YTFkMC0wZDFkLTRhY2ItYjQwOC1kNWNhNzMxMjFlOTAiXSwieG1zX3RjZHQiOjE2NzQxODQwNjN9.mLwVlkB_C6tD4tIu7cOo7vQKCZHhvy-umw7JCIy-7L6uWFwymNEzJchFmpZBc0tbv3gR-DCnWBOSF46eJUnORX-Qjac2blONwC_wJj-McSoq_Nx1YO-gkLsW28a052JoYcMwAxNcN2fs9iJ-7WGoTpLkkyBQqCVoTg9JszsLYO-6Usfj8mCNKxpvtaikSlBthY2XSOiXAl_dN9xb9qx6mOB0QOhHnvHav8SiG9wDIOGBdKBD3DcQBAR3PPbPZn5TlO-tS7NqH6-itWpRIdry6e0EQxNNHNB2s6NP0UPy8gBTmn7VHDwEeoJiV23SpLw7b0jnbaX2UTt2uHtW4xTSaw"

# Define the URL to get the OneDrive metadata
url = "https://graph.microsoft.com/v1.0/me/drive/root:/Pictures:/search(q='evony')"

# Set the query parameters to select only the file name and ID
query_params = {
    "select": "name,id",
    "top": 50
}

# Define the headers with the access token
headers = {
    "Authorization": f"Bearer {access_token}"
}

# Send the GET request to OneDrive
response = requests.get(url, headers=headers, params=query_params)

# Parse the response JSON into a dictionary
drive_response_data = response.json()

# Check if the response contains any files
if 'value' in drive_response_data:
    # Create a folder on the desktop to save the files
    os.makedirs("C:/Users/YOUR_USERNAME/Desktop/Evony", exist_ok=True)

    # Iterate over each file and download it
    for file in drive_response_data['value']:
        file_name = file['name']
        file_id = file['id']

        # Define the download URL for the file
        download_url = f"https://graph.microsoft.com/v1.0/me/drive/items/{file_id}/content"

        # Set the headers with the access token and the desired file format (JPEG or PNG)
        file_extension = os.path.splitext(file_name)[1]
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": f"image/{file_extension[1:].lower()}",
        }

        # Send the GET request to download the file
        response = requests.get(download_url, headers=headers)

        # Save the file to the "Evony" folder on the desktop
        with open(f"C:/Users/cdreh/Desktop/Evony/{file_name}", "wb") as f:
            f.write(response.content)

        # Print a message indicating that the file was downloaded and saved
        print(f"Downloaded and saved file: {file_name}")

else:
    # If there are no files, print a message
    print("No files found.")
