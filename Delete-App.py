#removes songs that are in the combined playlist but not in any of the user specified playlists


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
            print(song)
            deleteList.append(song)


    print('deleting {} songs'.format(len(deleteList)))
    sp.playlist_remove_all_occurrences_of_items(ePlaylist, deleteList)
    
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

    playlistNumLabel = ttk.Label(frame, text='How many total playlists do you have?').grid(row=0, pady=2)
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

    ePlaylistLabel = ttk.Label(frame, text='Enter the url of the playlist all the other playlists are combined into:').grid(row=0, pady=2)
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
