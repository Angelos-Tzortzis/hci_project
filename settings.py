import customtkinter


class settings(customtkinter.CTkToplevel):  # CTk για να το τρέξω έξω απο το main.py.
    def __init__(self):
        super().__init__()
        self.geometry("900x250")
        customtkinter.set_default_color_theme("blue")
        customtkinter.set_appearance_mode("dark")
        self.title("Settings")
        self.lift()
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, "-topmost", True)
        self.focus_set()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=1)

        self.dark_button = customtkinter.CTkButton(
            self, text="Dark Mode", command=self.change_to_dark
        )
        self.dark_button.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        self.light_button = customtkinter.CTkButton(
            self, text="Light Mode", command=self.change_to_light
        )
        self.light_button.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    def change_to_light(self):
        customtkinter.set_appearance_mode("light")

    def change_to_dark(self):
        customtkinter.set_appearance_mode("dark")


if __name__ == "__main__":
    app = settings()
    app.mainloop()
