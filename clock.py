from tkinter import *
from tkinter import messagebox
import time
import threading
from pygame import mixer
from PIL import Image, ImageTk, ImageSequence  # Import Pillow

root = Tk()
root.title("Alarm")
root.geometry("950x750")
root.configure(bg='#000000')  # Set background color to black

mixer.init()

# Start the thread
def th():
    t1 = threading.Thread(target=a, args=())
    t1.start()

# Function for the alarm
def a():
    alarm_time = hr.get()
    if alarm_time == "":
        messagebox.showerror('Invalid data', 'Please enter a valid time')
    else:
        while True:
            current_time = time.strftime("%H:%M")
            if alarm_time == current_time:
                try:
                    mixer.music.load('audio.mp3')  # Ensure the file extension matches your file
                    mixer.music.play()
                    msg = messagebox.showinfo('It is time', f'{amsg.get()}')
                    if msg == 'ok':
                        mixer.music.stop()
                    break
                except Exception as e:
                    messagebox.showerror('Error', f'Could not play alarm sound: {str(e)}')
            time.sleep(1)  # Sleep to prevent excessive CPU usage

header = Frame(root, bg='#000000')  # Set background color to black
header.pack(pady=20)  # Adjust padding as needed

head = Label(header, text="ALARM CLOCK", font=('comic sans', 28, 'bold'), bg='#000000', fg='#FFFFFF')  # Changed font to bold
head.pack(fill=X, padx=10, pady=10)

panel = Frame(root, bg='#000000')  # Set background color to black
panel.pack(pady=20)  # Adjust padding as needed

# Function to animate the GIF
def animate_gif(img_label, gif_frames, frame_index):
    frame = gif_frames[frame_index]
    img_label.configure(image=frame)
    frame_index = (frame_index + 1) % len(gif_frames)
    root.after(500, animate_gif, img_label, gif_frames, frame_index)  # Adjust the delay for smoother animation

# Use PIL to open and display the image
gif_path = 'clocee.gif'
gif = Image.open(gif_path)
gif_frames = [ImageTk.PhotoImage(frame.copy().resize((300, 300), Image.Resampling.LANCZOS)) for frame in ImageSequence.Iterator(gif)]

alp = Label(panel, bg='#000000')  # Set background color to black
alp.grid(row=0, column=0, rowspan=6, columnspan=2, padx=20, pady=(0, 10), sticky='nsew')  # Move image to the center and span across columns

# Start the GIF animation
animate_gif(alp, gif_frames, 0)

atime = Label(panel, text="Alarm Time (Hr:Min)", font=('comic sans', 18), bg='#000000', fg='#FFFFFF')  # Set background color to black and text color to white
atime.grid(row=6, column=0, padx=10, pady=(20, 5), sticky='e')  # Moved slightly down and aligned to the right

hr = Entry(panel, font=('comic sans', 20), width=5, justify='center', bg='#FFFFFF', fg='#000000')  # Set background color to white and text color to black
hr.grid(row=6, column=1, padx=10, pady=(20, 5), sticky='w')  # Moved slightly down and aligned to the left

amessage = Label(panel, text="Message", font=('comic sans', 20), bg='#000000', fg='#FFFFFF')  # Set background color to black and text color to white
amessage.grid(row=7, column=0, padx=10, pady=5, sticky='e')

amsg = Entry(panel, font=('comic sans', 15), width=25, justify='center', bg='#FFFFFF', fg='#000000')  # Set background color to white and text color to black
amsg.grid(row=7, column=1, padx=10, pady=5, sticky='w')

start = Button(panel, text="Start alarm", font=('comic sans', 20), command=th, bg='#FF4500', fg='#FFFFFF')  # Set background color to orange and text color to white
start.grid(row=8, column=0, columnspan=2, padx=10, pady=20)

root.mainloop()
