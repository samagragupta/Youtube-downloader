import pytube
import tkinter as tk

window = tk.Tk()
window.title("YouTube Downloader")

def downloader():
	link=str(entry.get())
	yt = pytube.YouTube(link)
	stream = yt.streams.first()
	destination="E:\Movies"
	stream.download(destination)

title=tk.Label(text="Welcome to YouTube Downloader.",font=40)
title.grid(column=0,row=0,padx=10, pady=10)

label=tk.Label(text="Please Enter the link of the video")
label.grid(column=0,row=1,padx=10, pady=10)

entry=tk.Entry()
entry.grid(column=0,row=2)

button=tk.Button(text="Click Here",font=15,bg="red",command=downloader)
button.grid(column=0,row=3,padx=10, pady=10)

window.mainloop()
