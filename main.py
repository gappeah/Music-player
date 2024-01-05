#impoorted libraries for music player with a modern GUI
import tkinter as tk
import os
import pygame
import time 
import customtkinter
from tkinter import filedialog
from tkinter import ttk



root = tk.Tk()
root.title("Music Player")
root.geometry("400x200")

def play_music():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            update_song_details()
        except Exception as e:
            print(e)

def stop_music():
    pygame.mixer.music.stop()
    progress_bar.stop()

def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True

def choose_file():
    global file_path
    file_path = filedialog.askopenfilename()

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    file_path = songs[current_song_index]
    play_music()

def prev_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    file_path = songs[current_song_index]
    play_music()

def update_song_details():
    song_name.set(file_path.split('/')[-1])

def set_volume(val):
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)

# UI Elements
play_button = tk.Button(root, text="Play", command=play_music)
play_button.grid(row=0, column=0, padx=10, pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.grid(row=0, column=1, padx=10, pady=10)

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.grid(row=0, column=2, padx=10, pady=10)

choose_file_button = tk.Button(root, text="Choose File", command=choose_file)
choose_file_button.grid(row=1, columnspan=3, padx=10, pady=10)

prev_button = tk.Button(root, text="Previous", command=prev_song)
prev_button.grid(row=2, column=0, padx=10, pady=10)

next_button = tk.Button(root, text="Next", command=next_song)
next_button.grid(row=2, column=2, padx=10, pady=10)

volume_label = tk.Label(root, text="Volume:")
volume_label.grid(row=3, column=0, padx=10, pady=10)

volume_slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=set_volume)
volume_slider.set(70)  # default volume
volume_slider.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

song_name = tk.StringVar()
song_label = tk.Label(root, textvariable=song_name)
song_label.grid(row=4, columnspan=3, padx=10, pady=10)

# Progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate")
progress_bar.grid(row=5, columnspan=3, padx=10, pady=10)

file_path = ""
songs = []  # Add your music file paths here
current_song_index = 0
paused = False

pygame.mixer.init()

root.mainloop()
