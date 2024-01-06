#imported libraries for music player with a modern GUI
import tkinter as tk
import pygame
import customtkinter
from tkinter import filedialog
from tkinter import ttk
from mutagen.mp3 import MP3
#import ttkbootstrap as ttk

root = customtkinter.CTk()
root.title("Music Player")
root.geometry("750x500")

def play_music():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        try:
            pygame.mixer.music.load(file_paths[current_song_index])
            pygame.mixer.music.play()
            update_song_details()
            update_length()
            start_countdown()
        except Exception as e:
            print(e)

def stop_music():
    pygame.mixer.music.stop()
    progress_bar.stop()
    timer_label.configure(text="")

def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True

def choose_files():
    global file_paths, current_song_index
    file_paths = filedialog.askopenfilenames()
    current_song_index = 0
    if file_paths:
        play_music()

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(file_paths)
    play_music()

def prev_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(file_paths)
    play_music()

def update_song_details():
    song_name.set(file_paths[current_song_index].split('/')[-1])

def update_length():
    global song_length
    audio = MP3(file_paths[current_song_index])
    song_length = audio.info.length

def start_countdown():
    global song_length
    while pygame.mixer.music.get_busy():
        current_time = pygame.mixer.music.get_pos() / 1000
        minutes, seconds = divmod(current_time, 60)
        timer_label.configure(text=f"Time Elapsed: {int(minutes)}:{int(seconds)} / {int(song_length // 60)}:{int(song_length % 60)}")
        root.update()
        progress = (current_time / song_length) * 100
        progress_bar['value'] = progress
        root.after(1000)


def set_volume(val):
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)

# UI Elements
customtkinter.set_default_color_theme("green")

choose_file_button = customtkinter.CTkButton(root, text="Choose Files", fg_color="#1DB954", command=choose_files)
choose_file_button.pack(pady=10)

prev_button = customtkinter.CTkButton(root, text="Previous", fg_color="#1DB954", command=prev_song)
prev_button.pack(pady=5)

play_button = customtkinter.CTkButton(root, text="Play", fg_color="#1DB954", command=play_music)
play_button.pack(pady=5)

pause_button = customtkinter.CTkButton(root, text="Pause", fg_color="#1DB954", command=pause_music)
pause_button.pack(pady=5)

stop_button = customtkinter.CTkButton(root, text="Stop", fg_color="#1DB954", command=stop_music)
stop_button.pack(pady=5)

next_button = customtkinter.CTkButton(root, text="Next", fg_color="#1DB954", command=next_song)
next_button.pack(pady=5)

volume_label = customtkinter.CTkLabel(root, text="Volume:")
volume_label.pack(pady=5)

volume_slider = customtkinter.CTkSlider(root, from_=0, to=100, orientation="horizontal",progress_color="#1DB954", fg_color="gray", command=set_volume)
volume_slider.set(50)  # default volume
volume_slider.pack(pady=5)

song_name = tk.StringVar()
song_label = customtkinter.CTkLabel(root, textvariable=song_name)
song_label.pack(pady=5)

timer_label = customtkinter.CTkLabel(root, text="Time Elapsed:")
timer_label.pack(pady=5)

# Progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate", length=400)
progress_bar.pack(pady=10)

file_paths = []
current_song_index = 0
paused = False
song_length = 0

pygame.mixer.init()

root.mainloop()
