import tkinter as tk

class GenericPage(tk.Frame):
    background = None
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, **kwargs, background=self.background)