from tkinter import *
import tkinter
from pytube import YouTube
win= Tk()

win.geometry("350x200")
win.title("Youtube downloader")
win.configure(bg="yellow")
label=Label(win, text="", font=("Courier 16 bold"),bg="yellow")
label.grid(row=8, column=1)
link_text = Label(win, text="Link: ",bg="gold")
link_text.grid(row=1, column=0, padx=7, pady=20)

entry= Entry(win, width=45, bd=5, bg="green")
entry.grid(row=1, column=1, pady=20)


def display_text():
   global entry
   link = entry.get()
   label.configure(text="The video downloaded:)")
   yt = YouTube(link)
   y_d = yt.streams.get_highest_resolution()
   y_d.download('C:/Users/shahboz/Videos/youtube')
button = tkinter.Button(win,text="Download",width= 20,command= display_text, 
                        bg="green",activebackground="grey")
button.grid(row=5, column=1)

win.mainloop()