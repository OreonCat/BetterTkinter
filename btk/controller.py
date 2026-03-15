import tkinter as tk

from btk.pages import GenericPage


class Controller(tk.Tk):
    preloaded_pages = []
    title_page = None
    height = 100
    width = 100
    start_page = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(self.title_page)
        self.geometry(f"{self.height}x{self.width}")
        self.frames = {}

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.make_container()
        self.show_frame(self.start_page)

    def make_container(self):
        for page in self.preloaded_pages:
            frame = page(self.container, self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()



