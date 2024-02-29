from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import customtkinter
from customtkinter import *
from PIL import ImageTk, Image


class sms(customtkinter.CTkToplevel):  # CTk για να το τρέξω έξω απο το main.py.
    def __init__(self):
        super().__init__()
        self.geometry("460x900")
        self.resizable(False, False)
        customtkinter.set_default_color_theme("blue")
        customtkinter.set_appearance_mode("dark")
        self.title("SMS")
        self.lift()
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, "-topmost", False)
        self.focus_set()

        image = Image.open("sms.jpg")
        image = image.resize((460, 900), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        label = customtkinter.CTkLabel(self, image=photo)
        label.image = photo
        label.grid(row=0, column=0, columnspan=3, sticky="nsew")


if __name__ == "__main__":
    app = sms()
    app.mainloop()
