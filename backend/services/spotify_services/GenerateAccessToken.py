import requests
import base64
import SECRETS

client_id = SECRETS.CLIENT_ID
client_secret = SECRETS.CLIENT_SECRET

# Encode the client ID and secret
client_creds = f"{client_id}:{client_secret}"
client_creds_b64 = base64.b64encode(client_creds.encode()).decode()

# Set the token URL and headers
token_url = 'https://accounts.spotify.com/api/token'
headers = {
    'Authorization': f'Basic {client_creds_b64}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Set the data for the token request
data = {
    'grant_type': 'client_credentials'
}

# Make the request to get the access token
response = requests.post(token_url, headers=headers, data=data)
response_data = response.json()

# Extract the access token
access_token = response_data['access_token']