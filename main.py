import sqlite3
from PIL import Image, ImageTk
import os
import tkinter
import subprocess
import tkinter.messagebox
import customtkinter
import urllib.parse
import webbrowser
from customtkinter import *
from calendar_app import calendar_app
from e_mail import e_mail
from news import news
from music import music
from sms import sms
from phone import phone
from weather import weather
from traffic import traffic
from gps import gps
from settings import settings

API_KEY = "46f1942a35684436a2eaa05b27fd06d8"

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
        title_label.grid(row=0, column=0, columnspan=5, sticky="nsew")

        # Create grid.
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=5)
        self.rowconfigure(3, weight=5)

        # Functions to open services.
        def open_calendar():
            app = calendar_app()
            app.mainloop()

        def open_email():
            app = e_mail()
            app.mainloop()

        def open_news():
            app = news()
            app.mainloop()

        def web_search():
            google_url = "https://www.google.com/search?q="
            search_url = google_url + urllib.parse.quote(self.search.get())
            webbrowser.open(search_url)

        def open_music():
            app = music()
            app.mainloop()

        def open_sms():
            app = sms()
            app.mainloop()

        def open_phone():
            app = phone()
            app.mainloop()

        def open_weather():
            app = weather()
            app.mainloop()

        def open_traffic():
            app = traffic()
            app.mainloop()
        
        def open_gps():
            app = gps()
            app.mainloop()
        
        def open_settings():
            app = settings()
            app.mainloop()

        # Create buttons for each service.
        self.box1 = customtkinter.CTkButton(
            self,
            text="Calendar",
            fg_color="#5500ff",
            cursor="hand2",
            font=("TimeBurner", 20),
            command=open_calendar,
        )
        self.box1.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

        self.box2 = customtkinter.CTkButton(
            self,
            text="Music",
            fg_color="#5500ff",
            cursor="hand2",
            font=("TimeBurner", 20),
            command=open_music,
        )
        self.box2.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

        self.box3 = customtkinter.CTkButton(
            self,
            text="GPS",
            fg_color="#5500ff",
            cursor="hand2",
            font=("TimeBurner", 20),
            command=open_gps,
        )
        self.box3.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

        self.box4 = customtkinter.CTkButton(
            self,
            text="News",
            fg_color="#5500ff",
            cursor="hand2",
            font=("TimeBurner", 20),
            command=open_news,
        )
        self.box4.grid(row=3, column=1, sticky="nsew", padx=10, pady=10)

        self.box5 = customtkinter.CTkButton(
            self,
            text="Traffic",
            fg_color="#5500ff",
            cursor="hand2",
            font=("TimeBurner", 20),
        )
        self.box5.grid(row=2, column=2, sticky="nsew", padx=10, pady=10)

        self.box6 = customtkinter.CTkButton(
            self,
            text="Shop",
            fg_color="#5500ff",
            cursor="hand2",
            font=("TimeBurner", 20),
        )
        self.box6.grid(row=3, column=2, sticky="nsew", padx=10, pady=10)

        self.box7 = customtkinter.CTkButton(
            self,
            text="Email",
            fg_color="#5500ff",
            cursor="hand2",
            font=("TimeBurner", 20),
            command=open_email,
        )
        self.box7.grid(row=2, column=3, sticky="nsew", padx=10, pady=10)

        self.box8 = customtkinter.CTkButton(
            self,
            text="Maps",
            fg_color="#5500ff",
            cursor="hand2",
            font=("TimeBurner", 20),
        )
        self.box8.grid(row=3, column=3, sticky="nsew", padx=10, pady=10)

        self.box9 = customtkinter.CTkButton(
            self,
            text="SMS",
            fg_color="#5500ff",
            cursor="hand2",
            font=("TimeBurner", 20),
            command=open_sms,
        )
        self.box9.grid(row=2, column=4, sticky="nsew", padx=10, pady=10)

        self.box10 = customtkinter.CTkButton(
            self,
            text="Phone",
            fg_color="#5500ff",
            cursor="hand2",
            font=("TimeBurner", 20),
            command=open_phone,
        )
        self.box10.grid(row=3, column=4, sticky="nsew", padx=10, pady=10)

        self.box11 = customtkinter.CTkButton(
            self,
            text="Weather",
            fg_color="#5500ff",
            cursor="hand2",
            font=("TimeBurner", 20),
            command=open_weather,
        )
        self.box11.grid(row=2, column=5, sticky="nsew", padx=10, pady=10)

        self.box12 = customtkinter.CTkButton(
            self,
            text="Traffic",
            fg_color="#5500ff",
            cursor="hand2",
            font=("TimeBurner", 20),
            command=open_traffic,
        )
        self.box12.grid(row=3, column=5, sticky="nsew", padx=10, pady=10)

        self.search = customtkinter.CTkEntry(
            self,
            placeholder_text="search  [opens web browser]...",
            font=("TimeBurner", 20),
        )
        self.search.grid(row=1, column=0, columnspan=3, sticky="ew", padx=20)
        self.search.bind("<Return>", lambda event: web_search())

        self.search_button = customtkinter.CTkButton(
            self,
            text="Search",
            font=("TimeBurner", 20),
            command=web_search,
        )
        self.search_button.grid(row=1, column=3, sticky="w")

        self.settings_button = customtkinter.CTkButton(
            self,
            text="Settings",
            font=("TimeBurner", 20),
            fg_color="purple",
            command=open_settings,
        )
        self.settings_button.grid(row=1, column=5, sticky="")


if __name__ == "__main__":
    app = App()
    app.mainloop()
