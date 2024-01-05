#impoorted libraries for music player with a modern GUI
import tkinter as tk
import os
import pygame
import time 
import customtkinter

import pygame
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Music Player")

def play_music():
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(loops=0)

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def choose_file():
    global file_path
    file_path = filedialog.askopenfilename()

play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack()

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack()

unpause_button = tk.Button(root, text="Unpause", command=unpause_music)
unpause_button.pack()

choose_file_button = tk.Button(root, text="Choose File", command=choose_file)
choose_file_button.pack()

file_path = ""

pygame.mixer.init()

root.mainloop()
