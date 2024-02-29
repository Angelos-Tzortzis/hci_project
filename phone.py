import tkinter
import customtkinter


class phone(customtkinter.CTk):  # CTk για να το τρέξω έξω απο το main.py.
    def __init__(self):
        super().__init__()
        self.geometry("460x900")
        self.resizable(False, False)
        customtkinter.set_default_color_theme("blue")
        customtkinter.set_appearance_mode("dark")
        self.title("Phone")
        self.lift()
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, "-topmost", False)
        self.focus_set()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=2)
        self.rowconfigure(3, weight=2)
        self.rowconfigure(4, weight=2)
        self.rowconfigure(5, weight=1)

        self.entry = tkinter.Entry(self, font=("Arial", 20))
        self.entry.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)

        buttons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "0", "#"]

        row = 1
        column = 0
        for button_text in buttons:
            button = customtkinter.CTkButton(
                self,
                text=button_text,
                font=("timeburner", 20),
                command=lambda button_text=button_text: self.key_press(button_text),
            )
            button.grid(
                row=row,
                column=column,
                sticky="nsew",
                padx=5,
                pady=5,
            )
            column += 1
            if column > 2:
                column = 0
                row += 1

        self.call_button = tkinter.Button(
            self,
            text="Call",
            font=("Arial", 20),
            bg="green",
            fg="white",
            command=self.call,
        )
        self.call_button.grid(
            row=5, column=0, columnspan=1, sticky="nsew", padx=5, pady=5
        )

        self.delete_button = tkinter.Button(
            self,
            text="Delete",
            font=("Arial", 20),
            bg="red",
            fg="white",
            command=self.delete,
        )
        self.delete_button.grid(
            row=5, column=2, columnspan=1, sticky="nsew", padx=5, pady=5
        )

    def key_press(self, key):
        current_number = self.entry.get()
        new_number = current_number + key
        self.entry.delete(0, "end")
        self.entry.insert("end", new_number)

    def delete(self):
        current_number = self.entry.get()
        new_number = current_number[:-1]
        self.entry.delete(0, "end")
        self.entry.insert("end", new_number)

    def call(self):
        phone_number = self.entry.get()
        print(f"Calling {phone_number}")


if __name__ == "__main__":
    app = phone()
    app.mainloop()
