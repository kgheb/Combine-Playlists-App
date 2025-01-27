#removes songs that are in the combined playlist but not in any of the user's other playlists

import spotipy
import math
import time

#defines list of playlist urls that will be used
listOfPlaylists=[]

with open('token.txt') as file:
    token = file.read()
#authorizes the code so that the spotipy commands can be run as methods of "sp"
sp = spotipy.Spotify(auth=token)

#retrieves all the playlists of the user as dictionaries
userId=sp.current_user()['id']
playlistDicts = sp.user_playlists(userId)['items']

#creates a list of all the playlist urls
listOfPlaylists = []
for dict in playlistDicts:
    listOfPlaylists.append(dict['uri'])

#creates a dictionary of all the playlist names
listOfPlaylistNames = []
for dict in playlistDicts:
    listOfPlaylistNames.append(dict['name'])
dictOfPlaylistNames = {index: value for index, value in enumerate(listOfPlaylistNames)}
print(dictOfPlaylistNames)

#determines the index of the everything playlist
ePlaylistIndex = int(input('Enter the number that corresponds to the playlist you want to delete songs from: '))

print('')
print('Deleting songs now...')
#sets the variable of the everything playlist and removes it from the list
ePlaylist = listOfPlaylists[ePlaylistIndex]
listOfPlaylists.pop(ePlaylistIndex)
listOfPlaylistNames.pop(ePlaylistIndex)

totalSongList = []

for playlist in listOfPlaylists:
    index = 0
     #defines the repeat times that will be used to make the song list
    repeatTimes = math.ceil(sp.playlist_tracks(playlist, 'total')['total']/100)
    for i in range(repeatTimes):
            dictList = ((sp.playlist_tracks(playlist, 'items.track.uri', offset = index))['items'])
            for item in dictList:
                totalSongList.append(item['track']['uri'])
            index +=100

eSongList = []

eRepeatTimes = math.ceil(sp.playlist_tracks(ePlaylist, 'total')['total']/100)

index = 0
for i in range(eRepeatTimes):
    dictList = ((sp.playlist_tracks(ePlaylist, 'items.track.uri', offset = index))['items'])
    for item in dictList:
        eSongList.append(item['track']['uri'])
    index +=100

deleteList=[]

for song in eSongList:
    if song not in totalSongList:
        deleteList.append(song)
        
if deleteList != []:
    sp.playlist_remove_all_occurrences_of_items(ePlaylist, deleteList)
    print('Deleted '+str(len(deleteList))+' songs')
else:
    print('No songs to delete')

time.sleep(5)
