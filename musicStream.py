import tkinter as tk
import pygame
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, window):
        window.geometry('320x100'); window.title('Music Player'); window.resizable(1,1)
        pygame.init()
        pygame.mixer.init()
        self.track = tk.StringVar()
        self.status = tk.StringVar()

        # Creating the Track Frames for Song label & status label
        trackframe = tk.LabelFrame(window, text="Song Track", font=("times new roman",15,"bold"), bg="Navyblue", fg="white", bd=5, relief=tk.GROOVE)
        trackframe.place(x=0, y=0, width=600, height=100)
        # Inserting Song Track Label
        songtrack = tk.Label(trackframe, textvariable=self.track, width=20, font=("times new roman", 24, "bold"), bg="Orange", fg="gold").grid(row=0, column=0, padx=10, pady=5)
        # Inserting Status Label
        trackstatus = tk.Label(trackframe, textvariable=self.status, font=("times new roman", 24, "bold"), bg="orange", fg="gold").grid(row=0, column=1, padx=10, pady=5)

        # Creating Button Frame
        buttonframe = tk.LabelFrame(window, text="Control Panel", font=("times new roman",15,"bold"), bg="grey", fg="white", bd=5, relief=tk.GROOVE)
        buttonframe.place(x=0, y=100, width=600, height=100)
        # Inserting Play Button
        playbtn = tk.Button(buttonframe, text="PLAY", command=self.playsong, width=6, height=1, font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=0, padx=10, pady=5)
        # Inserting Pause Button
        playbtn = tk.Button(buttonframe, text="PAUSE", command=self.pausesong, width=8, height=1, font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=1, padx=10, pady=5)
        # Inserting Stop Button
        playbtn = tk.Button(buttonframe, text="STOP", command=self.stopsong, width=6, height=1, font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=2, padx=10, pady=5)
        # Inserting Open Button
        playbtn = tk.Button(buttonframe, text="OPEN", command=self.open_file, width=6, height=1, font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=3, padx=10, pady=5)

    def open_file(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=(("wav files", "*.wav"), ("all files", "*.*")))
        self.track.set(self.filename)
        self.status.set("-Playing")

    def playsong(self):
        pygame.mixer.music.load(self.filename)
        pygame.mixer.music.play()

    def stopsong(self):
        pygame.mixer.music.stop()
        self.status.set("-Stopped")

    def pausesong(self):
        pygame.mixer.music.pause()
        self.status.set("-Paused")

root = tk.Tk()
MusicPlayer(root)
root.mainloop()