import tkinter
import customtkinter
from pytube import YouTube

def initDownload():
    status = customtkinter.CTkLabel(app, text='')
    status.pack(padx = 10, pady = 10)
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=onProgress) 
        dVideo = ytObject.streams.get_highest_resolution()
        dVideo.download() 
        status.configure(text='Downloaded')
    except:
        status.configure(text='Something went wrong!')

def onProgress(stream, chunk, remainingBytes):
    totalSize = stream.filesize
    bytesDownloaded = totalSize - remainingBytes
    percToCompletion = int(bytesDownloaded / totalSize * 100)
    progressPerc.configure(text = f'{percToCompletion}%')
    progressPerc.update()
    progressBar.set(float(percToCompletion)/100)
    
        
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.geometry('600x280')
app.title('Youtube Video Downloader')

#Ui
title= customtkinter.CTkLabel(app, text= 'YouTube Video Downloader', font=('Roboto', 24, 'bold'))
title.pack(padx=10, pady=25)


urlVar = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=urlVar, placeholder_text='Enter YouTube link...',fg_color= 'transparent', border_color ='#52527a',border_width = 1.2, corner_radius= 0)
link.pack()

progressBar = customtkinter.CTkProgressBar(app, width = 350, corner_radius= 0, progress_color= '#1ac6ff')
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

progressPerc = customtkinter.CTkLabel(app, text='0%')
progressPerc.pack(pady = 0)

dButton = customtkinter.CTkButton(app, text ='Download', height=40, corner_radius= 0, fg_color= 'transparent', border_color='#1ac6ff', border_width=1.2, command = initDownload)
dButton.pack(padx = 0, pady = 0)

app.mainloop()