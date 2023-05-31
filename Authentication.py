import spotipy
from spotipy.oauth2 import SpotifyOAuth

#sets variables; get from spotify developer website
with open('client-id.txt') as file:
    clientId = file.read()
with open('client-secret.txt') as file:
    clientSecret = file.read()
redirectUri='https://localhost/'
#sets scopes to allow code to edit spotify playlists
scopes = ['playlist-modify-public', 'playlist-modify-private']

token = spotipy.util.prompt_for_user_token(scope=scopes, client_id=clientId, client_secret=clientSecret, redirect_uri=redirectUri, show_dialog=True)

with open('token.txt', 'w+') as file:
    file.write(token)