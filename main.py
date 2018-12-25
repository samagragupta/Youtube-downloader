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

window.mainloop()
