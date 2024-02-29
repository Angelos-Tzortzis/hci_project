import requests
import customtkinter
from PIL import Image, ImageTk
from io import BytesIO
import webbrowser


API_KEY = "7a22878f03004754ae372da20448d5e9"
golbal_image = None


class news(customtkinter.CTkToplevel):  # CTk για να το τρέξω έξω απο το main.py.
    def __init__(self):
        global golbal_image
        super().__init__()
        self.geometry("960x480")
        customtkinter.set_default_color_theme("blue")
        customtkinter.set_appearance_mode("dark")
        self.title("News")
        self.lift()
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, "-topmost", False)
        self.focus_set()

        title_label = customtkinter.CTkLabel(self, text="News", font=("TimeBurner", 35))
        title_label.grid(row=0, column=0, sticky="nsew")

        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=50)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        self.articles = self.get_news()

        image_url = self.articles["urlToImage"]
        image_data = requests.get(image_url).content
        image1 = Image.open(BytesIO(image_data))
        global_image = ImageTk.PhotoImage(image1)
        self.image_label = customtkinter.CTkLabel(self, text="", image=global_image)
        self.image_label.grid(
            row=2, column=0, rowspan=5, sticky="nsew", padx=10, pady=10
        )

        title = self.articles["title"]
        self.title_label = customtkinter.CTkLabel(
            self, text=title, font=("TimeBurner", 17)
        )
        self.title_label.grid(row=1, column=0, sticky="s")

        if self.articles["content"] is None:
            self.articles["content"] = ""
        # Getting only the first line of code to display, and if the window is fullscreen print the first paragraph.
        content_lines = (
            self.articles["content"].split("\n") if title is not None else [""]
        )
        first_line = "\n".join(content_lines[:2])

        text_label = customtkinter.CTkLabel(
            self,
            text=first_line,
            justify="center",
            wraplength=500,
        )
        text_label.grid(row=3, column=0, sticky="nsew")

        self.link_label = customtkinter.CTkLabel(
            self,
            text="Read More...",
            cursor="hand2",
            font=("Arial bold", 14),
            text_color="#6da1ca",
        )
        self.link_label.bind(
            "<Button-1>",
            lambda e: webbrowser.open_new(self.articles["url"]),
        )
        self.link_label.grid(row=4, column=0, sticky="nsew")

    def get_news(self):
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        articles = data["articles"]
        return articles[-1]


if __name__ == "__main__":
    app = news()
    app.mainloop()
