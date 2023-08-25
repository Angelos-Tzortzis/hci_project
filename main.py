import sqlite3
from PIL import Image, ImageTk
import os
import tkinter
import subprocess
import tkinter.messagebox
import customtkinter
from customtkinter import *
from Calendar import CalendarApp
from Music import MusicPlayer
from Search import search_query
from News import NewsWidget
from traffic import TrafficWidget
from MyShop import MyShop
from mail import EmailApp
from maps import Maps
from Music import MusicPlayer

# Modes: "System" (standard), "Dark", "Light"
# Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Configure window
        self.geometry("1080x720")
        customtkinter.set_default_color_theme("blue")
        customtkinter.set_appearance_mode("dark")
        self.title("Virtual Assistant")

        title_label = customtkinter.CTkLabel(
            self, text="Virtual Assistant", font=("TimeBurner", 30)
        )
        title_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Create grid.
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=5)
        self.rowconfigure(2, weight=5)

        # Create buttons for each service.
        self.box1 = customtkinter.CTkButton(
            self,
            text="Calendar",
            fg_color="#5500ff",
            cursor="hand2",
            font=("TimeBurner", 20),
        )
        self.box1.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

        self.box2 = customtkinter.CTkButton(
            self,
            text="Music",
            fg_color="#5500ff",
            cursor="hand2",
            font=("TimeBurner", 20),
        )
        self.box2.grid(row=2, column=0, sticky="nsew", padx=20, pady=20)

        self.box3 = customtkinter.CTkButton(
            self,
            text="Search",
            fg_color="#5500ff",
            cursor="hand2",
            font=("TimeBurner", 20),
        )
        self.box3.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

        self.box4 = customtkinter.CTkButton(
            self,
            text="News",
            fg_color="#5500ff",
            cursor="hand2",
            font=("TimeBurner", 20),
        )
        self.box4.grid(row=2, column=1, sticky="nsew", padx=20, pady=20)

        self.box5 = customtkinter.CTkButton(
            self,
            text="Traffic",
            fg_color="#5500ff",
            cursor="hand2",
            font=("TimeBurner", 20),
        )
        self.box5.grid(row=1, column=2, sticky="nsew", padx=20, pady=20)

        self.box6 = customtkinter.CTkButton(
            self,
            text="Shop",
            fg_color="#5500ff",
            cursor="hand2",
            font=("TimeBurner", 20),
        )
        self.box6.grid(row=2, column=2, sticky="nsew", padx=20, pady=20)

        self.box7 = customtkinter.CTkButton(
            self,
            text="Email",
            fg_color="#5500ff",
            cursor="hand2",
            font=("TimeBurner", 20),
        )
        self.box7.grid(row=1, column=3, sticky="nsew", padx=20, pady=20)

        self.box8 = customtkinter.CTkButton(
            self,
            text="Maps",
            fg_color="#5500ff",
            cursor="hand2",
            font=("TimeBurner", 20),
        )
        self.box8.grid(row=2, column=3, sticky="nsew", padx=20, pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
