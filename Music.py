import customtkinter
from PIL import Image, ImageTk
import os
import pygame
import mutagen.mp3
from PIL import Image, ImageTk
from tkinter import PhotoImage
from typing import Union
import customtkinter

pygame.mixer.init()


class music(customtkinter.CTkToplevel):  # CTk για να το τρέξω έξω απο το main.py.
    def __init__(self):
        super().__init__()
        self.geometry("960x480")
        customtkinter.set_default_color_theme("blue")
        customtkinter.set_appearance_mode("dark")
        self.title("Music")
        self.lift()
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, "-topmost", False)
        self.focus_set()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        self.title_label = customtkinter.CTkLabel(
            self, text="Music", font=("TimeBurner", 30)
        )
        self.title_label.grid(row=0, column=0, columnspan=3, sticky="nsew")

        self.play_image = PhotoImage(file="play.png")
        self.pause_image = PhotoImage(file="pause.png")
        self.rewind_image = PhotoImage(file="rewind.png")
        self.fastforward_image = PhotoImage(file="fastforward.png")

        self.playing = False
        self.active_now = 0
        self.position = 0
        self.length = 0
        self.manual_position = False
        self.position = 0
        self.total_length = 0

        self.progress_bar = customtkinter.CTkSlider(self, command=self.change_position, from_=0, to=1)
        self.progress_bar.grid(row=4, column=0, columnspan=3, sticky="nsew")

        self.song_label = customtkinter.CTkLabel(
            self, text=self.audio_files[0], font=("TimeBurner", 20)
        )
        self.song_label.grid(row=2, column=0, columnspan=4, sticky="nsew")

        self.rewind_button = customtkinter.CTkButton(
            self, text="",command=self.previous, fg_color="white", cursor="hand2", image=self.rewind_image
        )
        self.rewind_button.grid(row=3, column=0, sticky="nsew", padx=10)

        self.play_button = customtkinter.CTkButton(
            self, text="", command=self.play, fg_color="white", cursor="hand2", image=self.play_image
        )
        self.play_button.grid(row=3, column=1, sticky="nsew", padx=10)

        self.fastforward_button = customtkinter.CTkButton(
            self,
            text="",
            command=self.next,
            fg_color="white",
            cursor="hand2",
            image=self.fastforward_image,
        )
        self.fastforward_button.grid(row=3, column=2, sticky="nsew", padx=10)

        image = Image.open(f"{self.audio_files[0]}.jpg")
        image = image.resize((300, 300))
        self.song_image = ImageTk.PhotoImage(image)
        self.song_image_label = customtkinter.CTkLabel(self, image=self.song_image, text="")
        self.song_image_label.grid(row=1, column=0, columnspan=3, sticky="nsew")

        
        self.check_music()
        self.update_progress()

    audio_files = [
        "Led Zeppelin - Rock and Roll.mp3",
        "Madvillain - All Caps.mp3",
    ]

    def music_now(self, index, audio_files) -> str:
        return audio_files[index]

    def change_position(self, position: Union[int, str]) -> None:
        self.manual_position = True
        self.position = float(position)
        song = self.music_now(self.active_now, self.audio_files)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(start=self.position)

    def update_progress(self) -> None:
        if self.playing and not self.manual_position:
            new_time = pygame.mixer.music.get_pos() / 1000
            self.progress_bar.set(new_time)
            if abs(self.total_length - new_time) <= 1:
                self.next()
        elif not self.playing:
            self.manual_position = False
        self.after(1000, self.update_progress)

    def check_music(self):
        if not pygame.mixer.music.get_busy() and self.playing:
            self.next()
        self.after(100, self.check_music)
    
    def play(self, index: Union[int, str] = None) -> None:
        if self.playing:
            self.pause()
            return
        total_len_music = len(self.audio_files)
        if index is None:
            index = self.active_now
        elif index == total_len_music:
            index = 0
        self.playing = True
        song = self.music_now(index, self.audio_files)
        mp3 = mutagen.mp3.MP3(song)
        self.total_length = mp3.info.length
        self.progress_bar.configure(to=self.total_length)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        self.play_button.configure(image=self.pause_image, command=self.pause)
        self.update_image()
        self.update_song_title()
    
    def pause(self) -> None:
        self.playing = False
        pygame.mixer.music.pause()
        self.play_button.configure(image=self.play_image, command=self.unpause)
    
    def unpause(self) -> None:
        self.playing = True
        pygame.mixer.music.unpause()
        self.play_button.configure(image=self.pause_image, command=self.pause)
    
    def next(self) -> None:
        self.playing = False
        pygame.mixer.music.stop()
        self.active_now += 1
        if self.active_now >= len(self.audio_files):
            self.active_now = 0
        self.position = 0
        self.progress_bar.set(0)
        self.play(self.active_now)
        self.update_image()
        self.update_song_title()
    
    def previous(self) -> None:
        self.playing = False
        pygame.mixer.music.stop()
        self.active_now -= 1
        if self.active_now < 0:
            self.active_now = len(self.audio_files) - 1
        self.position = 0
        self.progress_bar.set(0)
        self.play(self.active_now)
        self.update_image()
        self.update_song_title()
    
    def update_image(self) -> None:
        song_key = self.audio_files[self.active_now]
        image_path = f"{song_key}.jpg"

        if os.path.exists(image_path):
            image = Image.open(image_path)
            image = image.resize((300, 300))
            self.song_image = ImageTk.PhotoImage(image)
        else:
            blank_image = Image.new("RGB", color="white")
            self.song_image = ImageTk.PhotoImage(blank_image)
        self.song_image_label.configure(image=self.song_image)
        self.song_image_label.image = self.song_image
    
    def update_song_title(self) -> None:
        song_key = self.audio_files[self.active_now]
        song_title = os.path.splitext(song_key)[0]
        self.song_label.configure(text=song_title)

if __name__ == "__main__":
    app = music()
    app.mainloop()
