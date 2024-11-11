import sys
import os

# Add the root directory of your project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
# from backend.services.spotify_services 
import GenerateAccessToken
import requests

access_token = GenerateAccessToken.access_token

headers = {
    'Authorization': f'Bearer {access_token}'
}

playlist_id = "27lLXi36Wlws8thpFS5HD0"  # Replace with your playlist ID
url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

def get_track_IDs(playlist_id):
    output = []
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        tracks = response.json().get('items', [])
        for track in tracks:
            track_info = track['track']
            track_id = track_info['id']
            track_name = track_info['name']
            artist_name = track_info['artists'][0]['name']
            output.append((track_id, track_name, artist_name))
    return output

if __name__ == "__main__":
    tracks = get_track_IDs(playlist_id)
    for track in tracks:
        print(f"Track ID: {track[0]}, Track Name: {track[1]}, Artist Name: {track[2]}")
