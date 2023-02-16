from tkinter import * # For Framework
from PIL import ImageTk, Image # For the images
from pytube import YouTube # For downloading
import os # For folders
from tkinter import filedialog # For folders
from tkinter import messagebox # For the messageboxes

# Creating Frameworks

frameYoutube = Tk()

frameYoutube.title("Youtube Video Downloader")

icon = PhotoImage(file='youtube.png')
frameYoutube.iconphoto(False,icon)

canvas = Canvas(frameYoutube,height=750,width=500)
canvas.pack()

top_frame = Frame(frameYoutube,bg="#f2f2f0")
top_frame.place(relx=0.05,rely=0.03,relwidth=0.90,relheight=0.25)

mid_frame = Frame(frameYoutube,bg="#c6c7c5")
mid_frame.place(relx=0.05,rely=0.3,relwidth=0.90,relheight=0.25)

bottom_frame = Frame(frameYoutube,bg="#c6c7c5")
bottom_frame.place(relx=0.05,rely=0.57,relwidth=0.90,relheight=0.39)

# Elemanları Ekliyoruz.

# Top Frame

    # Title
general_title = Label(top_frame,bg="#f2f2f0",text="Youtube Video Downloader",font=("Garamond",18,"bold"))
general_title.pack(padx=10,pady=10,anchor="n")
    
    # Youtube logo
img = ImageTk.PhotoImage(Image.open("yt1.png"))
img_label = Label(top_frame,image=img)
img_label.pack(padx=10,pady=10,side="bottom")

# Mid Frame

    # Label
url_title = Label(mid_frame,bg="#c6c7c5",text="Video URL",font=("Garamond",12,"bold"))
url_title.pack(padx=10,pady=10,anchor="n")

    # Url Field
url_field = Text(mid_frame,height=1,width=53)
url_field.tag_configure('style',foreground="#bfbfbf",font=("Didot",10,"bold"))
url_field.place(x=14,y=50)

    # Url Default Text
bos_metin = "Please insert the video URL..."
url_field.insert(END,bos_metin,'style')

    # Type Label
type_title = Label(mid_frame,bg="#c6c7c5",text="Select the download option:",font=("Garamond",13,"bold"))
type_title.place(x=135,y=100)

    # Radio Buttons mp-3, mp-4
var = IntVar()
mp3_radio = Radiobutton(mid_frame,text="Mp-3",variable=var,value=1,bg="#c6c7c5",font=("Didot",10,"bold"))
mp3_radio.place(x=60,y=150)

mp4_radio = Radiobutton(mid_frame,text="Mp-4",variable=var,value=2,bg="#c6c7c5",font=("Didot",10,"bold"))
mp4_radio.place(x=340,y=150)

# Bottom Frame

    # Labels
video_title_title = Label(bottom_frame,bg="#c6c7c5",text="Video Title",font=("Garamond",14,"bold"))
video_title_title.pack(padx=10,pady=10,anchor="n")

video_title_label = Label(bottom_frame,bg="#c6c7c5",text="...",font=("Didot",12,"bold"),fg="#737373")
video_title_label.pack(padx=10,pady=10,anchor="n")

    # Button
        # Func
def select_folder():
    path_select = filedialog.askdirectory()
    video_folder_label.config(text=path_select)
        # Folder Button
folder_button = Button(bottom_frame,text="Select Folder",font=("Garamond",12,"bold"),height=1,width=12,command=select_folder)
folder_button.pack(padx=10,pady=10,anchor="n")

video_folder_label = Label(bottom_frame,bg="#c6c7c5",fg="#737373",text="...",font=("Didot",12,"bold"))
video_folder_label.pack(padx=10,pady=10,anchor="n")

    # Buttons
        # Download Button
            # Button Func
def download_video():
    
    # Radio Button Controle
    try:
        # Getting the url and other things
        url = url_field.get("1.0","end") # Video URL
        my_video = YouTube(url) # Video
        folder = video_folder_label.cget("text") # Folder

        if var.get() == 1: # Mp-3 chosen.
            last_message = "Your video is being downloaded in mp-3 format. Please don't close the app until the video has been downloaded!" # messagebox message
            messagebox.showinfo("Success",last_message)

            # Mp-3
            mp3 = my_video.streams.filter(only_audio=True).first() # Get all mp3's take the first one.
            output = mp3.download(folder)
            base, ext = os.path.splitext(output) # Split the file text
            to_mp3 = base + ".mp3" # Converting to mp-3
            os.rename(output,to_mp3) # Rename the file
        
        elif var.get() == 2: # Mp-4 chosen
            last_message = "Your video is being downloaded in mp-4 format. Please don't close the app until the video has been downloaded!"
            messagebox.showinfo("Success!",last_message)

            # Mp-4
            mp4 = my_video.streams.get_highest_resolution().download(folder)

        else:
            last_message = "Please be sure that all the necessary blanks are filled."
            messagebox.showerror("Failed!",last_message)

    except Exception as err:
        lastt_message = "Video downloading operation has failed! Please be sure that you're inserting the correct URL."
        messagebox.showerror("Failed!",lastt_message)
    
    finally:
        frameYoutube.destroy()

            # Download Button
download_button = Button(bottom_frame,text="Download",height=3,width=15,font=("Garamond",12,"bold"),command=download_video)
download_button.place(x=260,y=200)
        
        # Check Button
            # Button Func
def check_video():

    try:
        url = url_field.get("1.0","end") # Video URL
        my_video = YouTube(url) # Video
        video_title = my_video.title
        video_title_label.config(text=video_title)
    
    except Exception as err:
        lastt_message = "No video found from this URL. Please be sure that you're inserting the correct URL."
        messagebox.showerror("Failed!",lastt_message)
    
            # Check Button
check_button = Button(bottom_frame,text="Check",height=3,width=15,font=("Garamond",12,"bold"),command=check_video)
check_button.place(x=40,y=200)

# Launch.

frameYoutube.mainloop()