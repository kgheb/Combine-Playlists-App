#takes all the playlists on a user's profile and combines them into one user-specified playlist

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
offset = 0
playlistDicts = sp.user_playlists(userId)['items']
while True:
    if len(playlistDicts)%50 == 0:
        offset += 50
        playlistDicts.append(sp.user_playlists(userId, offset = offset)['items'])
    else:
        break

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

while True:
    #determines the index of the everything playlist
    ePlaylistIndex = int(input('Enter the number that corresponds to the playlist you want to combine songs into: '))

    #confirms the user's selection
    print('')
    confirmation = input('You would like to add songs to the playlist titled \'{}\'? y/n: '.format(listOfPlaylistNames[ePlaylistIndex]))
    if confirmation == 'y':
        break
    else:
        print('')

print('')
print('Combining playlists now...')

#sets the variable of the everything playlist and removes it from the list
ePlaylist = listOfPlaylists[ePlaylistIndex]
listOfPlaylists.pop(ePlaylistIndex)
listOfPlaylistNames.pop(ePlaylistIndex)


for spPlaylist in listOfPlaylists:
    gPlaylist = spPlaylist
    #defines the song lists
    eSongList = []
    gSongList = []

    #defines the repeat times that will be used to make the song lists
    eRepeatTimes = math.ceil(sp.playlist_tracks(ePlaylist, 'total')['total']/100)
    gRepeatTimes = math.ceil(sp.playlist_tracks(gPlaylist, 'total')['total']/100)

    #defines the function that makes song lists
        #repeatTimes - the number of times the for loop in the function has to repeat to include all of the songs in the playlist
        #playlist - the playlist that the songs are being taken from
        #songList - the list that the song names will be added to
    def makeSongList(repeatTimes, playlist, songList):
        index = 0
        for i in range(repeatTimes):
            dictList = ((sp.playlist_tracks(playlist, 'items.track.uri', offset = index))['items'])
            for item in dictList:
                songList.append(item['track']['uri'])
            index +=100

    #runs the function on both the given and everything playlists
    makeSongList(gRepeatTimes, gPlaylist, gSongList)
    makeSongList(eRepeatTimes, ePlaylist, eSongList)

    #defines the list of songs that will be added to the everything playlist
    addList = []

    #checks if each song in the given playlist is in the everthing playlist - if it isn't, the song is added to the addList
    for song in gSongList:
        if song in eSongList:
            None
        else:
            addList.append(song)

    #adds the songs from the addList to the everything playlist and displays the number of songs added to a playlist
        #if the addList is empty, print a message saying which playlist's songs are in the everything playlist already
    aRepeatTimes = math.ceil(len(addList)/100)
    if addList != []:
        index = 0 
        for i in range(aRepeatTimes):
            sp.playlist_add_items(ePlaylist, addList[index:index+100])
            index += 100
        print("{} song(s) from the playlist \"{}\" succesfully added".format(len(addList), sp.playlist(gPlaylist, 'name')['name']))
    else:
        print("All the songs in the playlist \"{}\" are already in the everything playlist".format(sp.playlist(gPlaylist, 'name')['name']))

#declaring variables for liked songs
likedSongsList = []
offset=0
addList = []

#creating liked songs list
while True:
    likedSongsDicts = sp.current_user_saved_tracks(50, offset)['items']

    if len(likedSongsDicts)%50 == 0:
        for dict in likedSongsDicts:
            likedSongsList.append(dict['track']['uri'])
        offset += 50
    else:
        for dict in likedSongsDicts:
            likedSongsList.append(dict['track']['uri'])
        break

#adding liked songs to addlist
for song in likedSongsList:
    if song in eSongList:
        None
    else:
        addList.append(song)

#adding addlist to playlist
aRepeatTimes = math.ceil(len(addList)/100)
if addList != []:
    index = 0 
    for i in range(aRepeatTimes):
        sp.playlist_add_items(ePlaylist, addList[index:index+100])
        index += 100
    print("{} song(s) from \"Liked Songs\" succesfully added".format(len(addList)))
else:
    print("All the songs in \"Liked Songs\" are already in the everything playlist")

print(' ')
print('Done!')
time.sleep(5)