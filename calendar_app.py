import tkinter
import customtkinter
from tkcalendar import Calendar


class calendar_app(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("960x480")
        customtkinter.set_default_color_theme("blue")
        customtkinter.set_appearance_mode("dark")
        self.title("Calendar")

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=3)
        self.rowconfigure(4, weight=1)

        title_label = customtkinter.CTkLabel(
            self, text="Calendar", font=("TimeBurner", 20)
        )
        title_label.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=2)

        self.clndr = Calendar(self, selectmode="day", date_pattern="dd/MM/yyyy")
        self.clndr.grid(
            row=1, column=0, rowspan=3, columnspan=2, sticky="nsew", padx=2, pady=2
        )

        event_label = customtkinter.CTkLabel(
            self, text="Choose date from calendar:", font=("TimeBurner", 15)
        )
        event_label.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)

        self.entry = customtkinter.CTkEntry(
            self, placeholder_text="Enter event (time, event)", font=("TimeBurner", 15)
        )
        self.entry.grid(row=1, column=2, columnspan=2, sticky="nsew", padx=40, pady=2)

        self.add_event = customtkinter.CTkButton(
            self,
            text="Add event to calendar",
            font=("TimeBurner", 15),
            command=self.add_event,
        )
        self.add_event.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)

        self.listbox = tkinter.Listbox(self, font=("TimeBurner", 15))
        self.listbox.config(bg="#343638", fg="white")
        self.listbox.grid(row=3, column=2, columnspan=2, sticky="nsew", padx=2, pady=2)

        self.delete_event = customtkinter.CTkButton(
            self,
            text="Delete event from calendar",
            font=("TimeBurner", 15),
            fg_color="red",
            command=self.delete_event,
        )
        self.delete_event.grid(row=4, column=3, sticky="nsew", padx=2, pady=2)

        delete_label = customtkinter.CTkLabel(
            self, text="Choose event from list:", font=("TimeBurner", 15)
        )
        delete_label.grid(row=4, column=2, sticky="nsew", padx=2, pady=2)

        with open("appointments.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                self.listbox.insert(tkinter.END, line)

    def add_event(self):
        date = self.clndr.get_date()
        event = self.entry.get()

        if date and event:
            self.listbox.insert(tkinter.END, f"{date}: {event}")
            with open("appointments.txt", "a") as file:
                file.write(f"{date}: {event}\n")

    def delete_event(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected)
            with open("appointments.txt", "w") as file:
                for i in range(self.listbox.size()):
                    file.write(f"{self.listbox.get(i)}")


if __name__ == "__main__":
    app = calendar_app()
    app.mainloop()
