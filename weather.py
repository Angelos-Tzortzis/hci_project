import tkinter
import customtkinter
from tkintermapview import TkinterMapView
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import os
import time
from PIL import ImageTk, Image


class weather(customtkinter.CTkToplevel):  # CTk για να το τρέξω έξω απο το main.py.
    def __init__(self):
        super().__init__()
        self.geometry("1080x575")
        self.resizable(False, False)
        customtkinter.set_default_color_theme("blue")
        customtkinter.set_appearance_mode("dark")
        self.title("Weather")
        self.lift()
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, "-topmost", False)
        self.focus_set()

        image = Image.open("weather.png")
        image = image.resize((1080, 575), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        label = customtkinter.CTkLabel(self, image=photo)
        label.image = photo
        label.grid(row=0, column=0, columnspan=3, sticky="nsew")


if __name__ == "__main__":
    app = weather()
    app.mainloop()
