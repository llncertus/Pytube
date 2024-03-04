import customtkinter
import tkinter
import os
from pytube import  YouTube

def download():
   try:
           ytlink = url_bar.get()
           ytObject = YouTube(ytlink, on_progress_callback = on_progress)
           video = ytObject.streams.get_lowest_resolution()
           video.download("~/Downloads")
           label3 = customtkinter.CTkLabel(app, text="Download Succesfully", text_color="green")
           label3.pack(padx = 10, pady = 10)
   except:
          label2 = customtkinter.CTkLabel(app, text="Download Error", fg_color="gray", bg_color="red" )
          label.pack(padx = 10, pady = 10)

def on_progress(stream, chunk, bytes_remaining):
      total_size = stream.filesize
      bytes_downloaded = total_size - bytes_remaining
      persentage_complated = bytes_downloaded / total_size * 100
      per = str(int(persentage_complated))
      persentage.configure(text = per + "%")
      persentage.update()

      # Uptade Of Progress Bar
      progress_bar.set(float(persentage_complated)/100)

#System Settings

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App Frame

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Create GUI Objects

label = customtkinter.CTkLabel(app, text="İnsert an URL")
label.pack(padx = 10, pady = 10)

# Enter İnput

url_var = tkinter.StringVar()
url_bar = customtkinter.CTkEntry(app, width=400, height=40, textvariable=url_var)
url_bar.pack()

# Download Button

download_button = customtkinter.CTkButton(app, text="Download", command=download)
download_button.pack(padx = 10, pady = 10)

# Progress Bar
persentage = customtkinter.CTkLabel(app, text="0%")
persentage.pack()
progress_bar = customtkinter.CTkProgressBar(app, width=400, height=20)
progress_bar.pack(padx = 10, pady = 10)
progress_bar.set(0)
      
      

# Run App

app.mainloop()