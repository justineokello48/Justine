import os

from pygame import*
from pygame import mixer_music
from tkinter import*


def playsong():
    currentsong = playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("playing")
    mixer.music.play()

def Pausesong():
    songstatus.set("paused")
    mixer.music.play()

def stopsong():
    songstatus.set("stopped")
    mixer.music.play()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.play()

root = Tk()
root.title("Just-in player")

mixer.init()
songstatus = stringVar()
songstatus.set("choosing")

playlist = listbox( root, selectmode = SINGLE, bg = "DodgerBlue2 ", fg = "white", front = ('arial',15), width = 40)
playlist.grid(columnspan=5)
os.chdir(rc:\users\HP\music)
songs = os.listdir()
for S in songs:
    playlist.insert(END, S)

Playbtn = Button(root, text = "play", command = playsong)
playbtn.config(front=('arial',20),bg ="DodgerBlue2", fg = "white", padx = 7, pady = 7)
playbtn.grid(row = 1, column = 0

Playbtn = Button(root, text = "pause", command = pausesong)
playbtn.config(front=('arial',20),bg ="DodgerBlue2", fg = "white", padx = 7, pady = 7)
playbtn.grid(row = 1, column = 1)

Playbtn = Button(root, text = "stop", command = stopsong)
playbtn.config(front=('arial',20),bg ="DodgerBlue2", fg = "white", padx = 7, pady = 7)
playbtn.grid(row = 1, column = 2)

Playbtn = Button(root, text = "Resume", command = resumesong)
playbtn.config(front=('arial',20),bg ="DodgerBlue2", fg = "white", padx = 7, pady = 7)
playbtn.grid(row = 1, column = 3)

root.mainloop()

