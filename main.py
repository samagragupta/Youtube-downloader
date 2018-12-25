import pytube
import tkinter as tk
from tkinter import *
import tkinter.filedialog as filedialog
import os

window = tk.Tk()
window.title("YouTube Downloader")

def ok():
    if var.get() == '720p':
        return '22'
    if var.get() == '360p':
        return '18'
    if var.get() == '1080p':
        return '137'
    if var.get() == '240p':
        return '133'
    if var.get() == '144p':
        return '160'   
    if var.get() == 'audio':
        return '140'    


def directory():
    root = tk.Tk()
    root.withdraw()
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    return tempdir

def downloader():
	link=str(entry.get())
	yt = pytube.YouTube(link)
	stream = yt.streams.get_by_itag(ok())
	destination="E:\Movies"
	stream.download(directory())

title=tk.Label(text="Welcome to YouTube Downloader.",font=40)
title.grid(column=0,row=0,padx=10, pady=10)

label=tk.Label(text="Please Enter the link of the video")
label.grid(column=0,row=1,padx=10, pady=10)

entry=tk.Entry()
entry.grid(column=0,row=2)

button=tk.Button(text="Download",font=15,bg="red",command=downloader)
button.grid(column=2,row=3,padx=10, pady=10)

button2=tk.Button(text="Location",font=15,bg="green",command=directory)
button2.grid(column=1,row=3,padx=10, pady=10)

var = StringVar(window)
var.set("360p")

option = OptionMenu(window, var, "1080p", "720p", "360p", "240p","144p","audios")
option.grid(column=1,row=4,padx=10, pady=10)

window.mainloop()
