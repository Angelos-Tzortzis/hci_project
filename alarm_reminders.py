import json
import sqlite3
from tkinter import *
import tkinter
import customtkinter
from customtkinter import *
from PIL import Image, ImageTk


class alarms_reminders(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("960x480")
        customtkinter.set_default_color_theme("blue")
        customtkinter.set_appearance_mode("dark")
        self.title("Alarms & Reminders")


if __name__ == "__main__":
    app = alarms_reminders()
    app.mainloop()
