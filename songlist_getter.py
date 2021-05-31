import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'enter client id here'
client_secret = 'enter client secret here'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def getTrackNames(playlist_id):
    names = []
    playlist = sp.playlist(playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        names.append(track['name'])
    return names
