import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter
import customtkinter
from customtkinter import *
from PIL import Image, ImageTk


class e_shop(customtkinter.CTk):  # CTk για να το τρέξω έξω απο το main.py.
    def __init__(self):
        super().__init__()
        self.geometry("1080x720")
        customtkinter.set_default_color_theme("blue")
        customtkinter.set_appearance_mode("dark")
        self.title("E-Shop")
        self.lift()
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, "-topmost", False)
        self.focus_set()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=2)
        self.rowconfigure(3, weight=2)

        self.title_label = customtkinter.CTkLabel(
            self, text="E-Shop", font=("TimeBurner", 30)
        )
        self.title_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.grid(row=1, column=0, columnspan=2, rowspan=3, sticky="nsew")
        self.tabview.add("Shop")
        self.tabview.add("Cart")

        self.shop_frame = self.tabview.tab("Shop")
        self.shop_frame.columnconfigure(0, weight=1)
        self.shop_frame.columnconfigure(1, weight=1)
        self.shop_frame.columnconfigure(2, weight=1)
        self.shop_frame.columnconfigure(3, weight=1)

        self.shop_frame.rowconfigure(0, weight=1)
        self.shop_frame.rowconfigure(1, weight=1)

        shirt = customtkinter.CTkImage(
            light_image=Image.open("shirt.jpg"), size = (300, 300)
        )
        self.shop_frame.box1 = customtkinter.CTkButton(self.shop_frame, text="", image=shirt)
        self.shop_frame.box1.grid(row=0, column=0, sticky="nsew")

        shirt = customtkinter.CTkImage(
            light_image=Image.open("shirt.jpg"), size=(300, 300)
        )
        self.shop_frame.box1 = customtkinter.CTkButton(self.shop_frame, text="", image=shirt)
        self.shop_frame.box1.grid(row=0, column=1, sticky="nsew")

        shirt = customtkinter.CTkImage(
            light_image=Image.open("shirt.jpg"), size=(300, 300)
        )
        self.shop_frame.box1 = customtkinter.CTkButton(self.shop_frame, text="", image=shirt)
        self.shop_frame.box1.grid(row=0, column=2, sticky="nsew")

        shirt = customtkinter.CTkImage(
            light_image=Image.open("shirt.jpg"), size=(300, 300)
        )
        self.shop_frame.box1 = customtkinter.CTkButton(self.shop_frame, text="", image=shirt)
        self.shop_frame.box1.grid(row=0, column=3, sticky="nsew")

        shirt = customtkinter.CTkImage(
            light_image=Image.open("shirt.jpg"), size=(300, 300)
        )
        self.shop_frame.box1 = customtkinter.CTkButton(self.shop_frame, text="", image=shirt)
        self.shop_frame.box1.grid(row=1, column=0, sticky="nsew")

        shirt = customtkinter.CTkImage(
            light_image=Image.open("shirt.jpg"), size=(300, 300)
        )
        self.shop_frame.box1 = customtkinter.CTkButton(self.shop_frame, text="", image=shirt)
        self.shop_frame.box1.grid(row=1, column=1, sticky="nsew")

        shirt = customtkinter.CTkImage(
            light_image=Image.open("shirt.jpg"), size=(300, 300)
        )
        self.shop_frame.box1 = customtkinter.CTkButton(self.shop_frame, text="", image=shirt)
        self.shop_frame.box1.grid(row=1, column=2, sticky="nsew")

        shirt = customtkinter.CTkImage(
            light_image=Image.open("shirt.jpg"), size=(300, 300)
        )
        self.shop_frame.box1 = customtkinter.CTkButton(self.shop_frame, text="", image=shirt)
        self.shop_frame.box1.grid(row=1, column=3, sticky="nsew")


if __name__ == "__main__":
    app = e_shop()
    app.mainloop()
