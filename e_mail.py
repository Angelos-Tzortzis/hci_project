import tkinter
import customtkinter
import smtplib


class e_mail(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("960x480")
        customtkinter.set_default_color_theme("blue")
        customtkinter.set_appearance_mode("dark")
        self.title("E-mail")

        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=30)
        self.rowconfigure(7, weight=1)

        title_label = customtkinter.CTkLabel(
            self, text="Email", font=("TimeBurner", 20)
        )
        title_label.grid(row=0, column=0, sticky="nsew", pady=5)

        self.to_label = customtkinter.CTkLabel(
            self, text="To:", font=("TimeBurner", 15)
        )
        self.to_label.grid(row=1, column=0, sticky="sw", pady=2, padx=10)
        self.to_entry = customtkinter.CTkEntry(self, font=("arial", 15))
        self.to_entry.grid(row=2, column=0, sticky="new", pady=2, padx=10)

        self.subject_label = customtkinter.CTkLabel(
            self, text="Subject:", font=("TimeBurner", 15)
        )
        self.subject_label.grid(row=3, column=0, sticky="sw", pady=2, padx=10)
        self.subject_entry = customtkinter.CTkEntry(self, font=("arial", 15))
        self.subject_entry.grid(row=4, column=0, sticky="new", pady=2, padx=10)

        self.body_label = customtkinter.CTkLabel(
            self, text="Body:", font=("TimeBurner", 15)
        )
        self.body_label.grid(row=5, column=0, sticky="sw", pady=2, padx=10)

        self.message = tkinter.Text(self, font=("arial", 15))
        self.message.config(bg="#343638", fg="white")
        self.message.grid(row=6, column=0, rowspan=1, sticky="nsew", pady=2, padx=10)

        self.send_button = customtkinter.CTkButton(
            self, text="Send e-mail", font=("TimeBurner", 15), command=self.send_email
        )
        self.send_button.grid(row=7, column=0, sticky="nsw", pady=5, padx=10)

    def send_email(self):
        sender = "lkickitupanacho@gmail.com"
        receiver = self.to_entry.get()
        password = "exfxkirwygjeficp"

        subject = self.subject_entry.get()
        message = self.message.get("1.0", "end")

        text = f"Subject: {subject}\n\n{message}"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(sender, password)
        server.sendmail(sender, receiver, text)


if __name__ == "__main__":
    app = e_mail()
    app.mainloop()
