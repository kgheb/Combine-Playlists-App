#takes user-specified playlists and combines them into one user-specified playlist


from tkinter import *
from tkinter import ttk
import spotipy
import math

#defines list of playlist urls that will be used
listOfPlaylists=[]

with open('token.txt') as file:
    token = file.read()
#authorizes the code so that the spotipy commands can be run as methods of "sp"
sp = spotipy.Spotify(auth=token)

def runApp():
    root = Tk()
    root.title('Spotify App')

    frame = ttk.Frame(root, padding=20)
    frame.grid()

    s = ttk.Style()
    s.configure('.', background='bisque', font=('Times New Roman', 12))

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
            ttk.Label(frame, text="{} song(s) from the playlist \"{}\" succesfully added".format(len(addList), sp.playlist(gPlaylist, 'name')['name'])).grid()
        else:
            ttk.Label(frame, text="All the songs in the playlist \"{}\" are already in the everything playlist".format(sp.playlist(gPlaylist, 'name')['name'])).grid()
    
    ttk.Label(frame, text='Done!').grid()

    root.mainloop()
#home screen
def screen1():
    root = Tk()
    root.title('Spotify App')

    #when the submit button is pressed
    def submit():
        global numPlaylists
        #gets the number of playlists from the user input
        numPlaylists = numPlaylistsEntry.get()
        #closes the first screen
        root.destroy()
        #opens the next screen
        screen2()

    frame = ttk.Frame(root, padding=20)
    frame.grid()

    s = ttk.Style()
    s.configure('.', background='bisque', font=('Times New Roman', 12))

    playlistNumLabel = ttk.Label(frame, text='How many total playlists do you want to combine?').grid(row=0, pady=2)
    numPlaylistsEntry = StringVar()
    playlistNumEntry = ttk.Spinbox(frame, from_ = 1, to = 50, textvariable=numPlaylistsEntry).grid(row=1, pady=2)
    submitButton = ttk.Button(frame, text='Submit', command=submit).grid(row=2, pady=2)

    root.mainloop()

def screen2():
    root = Tk()
    root.title('Spotify App')

    frame = ttk.Frame(root, padding=20)
    frame.grid()

    s = ttk.Style()
    s.configure('.', background='bisque', font=('Times New Roman', 12))

    label = ttk.Label(frame, text='Enter the URL of each of your playlists below')
    label.grid(row=0)

    def submit():
        for i in range(0, int(numPlaylists)):
            #exec('playlist{} = StringVar()'.format(i))
            exec('listOfPlaylists.append(playlist{}.get())'.format(i))
        root.destroy()
        screen3()
        
    for i in range(0, int(numPlaylists)):
        exec('label{} = ttk.Label(frame, text=\'Playlist #{}: \').grid(row={}, pady=4)'.format(i, i+1, 2*i+1))
        exec('global playlist{}; playlist{} = StringVar()'.format(i, i))
        exec('entry{} = ttk.Entry(frame, textvariable=playlist{}, font=(\'Times New Roman\', 12)).grid(row={})'.format(i,i,2*i+2))

    submitButton = ttk.Button(frame, text='Submit', command=submit).grid(pady=4)

    root.mainloop()

def screen3():
    root = Tk()
    root.title('Spotify App')

    frame = ttk.Frame(root, padding=20)
    frame.grid()

    s = ttk.Style()
    s.configure('.', background='bisque', font=('Times New Roman', 12))

    def submit():
        global ePlaylist
        #gets the number of playlists from the user input
        ePlaylist = ePlaylistEntry.get()
        #closes the first screen
        root.destroy()
        screen4()

    ePlaylistLabel = ttk.Label(frame, text='Enter the url of the playlist you want all the other playlists to be combined into:').grid(row=0, pady=2)
    ePlaylistEntry = StringVar()
    ePlaylistEntryBox = ttk.Entry(frame, font= ('Times New Roman', 12), textvariable=ePlaylistEntry).grid(row=1, pady=2)
    
    submitButton = ttk.Button(frame, text='Submit', command=submit).grid(pady=4)
    root.mainloop()

def screen4():
    root = Tk()
    root.title('Spotify App')
    
    frame = ttk.Frame(root, padding=20)
    frame.grid()

    s = ttk.Style()
    s.configure('.', background='bisque', font=('Times New Roman', 12))

    def nextScreen():
        root.destroy()
        runApp()

    ttk.Label(frame, text='Your Playlists:').grid(pady=4)

    for playlist in listOfPlaylists:
        ttk.Label(frame, text=sp.playlist(playlist, 'name')['name']).grid(pady=4)

    ttk.Label(frame, text='Your Everything Playlist:').grid(pady=4)
    ttk.Label(frame, text=sp.playlist(ePlaylist, 'name')['name']).grid(pady=4)

    ttk.Button(frame, text='Run App', command=nextScreen).grid()
    
    root.mainloop()

screen1()
