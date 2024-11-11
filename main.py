import GenerateAccessToken
import requests

access_token = GenerateAccessToken.access_token

headers = {
    'Authorization': f'Bearer {access_token}'
}

playlist_id = "27lLXi36Wlws8thpFS5HD0"  # Replace with your playlist ID
url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

response = requests.get(url, headers=headers)
if response.status_code == 200:
    tracks = response.json().get('items', [])
    for track in tracks:
        track_info = track['track']
        track_id = track_info['id']
        track_name = track_info['name']
        artist_name = track_info['artists'][0]['name']
        print(f"Track ID: {track_id}, Song Name: {track_name}, Artist: {artist_name}")    
else:
    print(f"Failed to retrieve tracks: {response.status_code}")

