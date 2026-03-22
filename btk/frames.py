import tkinter as tk
from tkinter import ttk


class GenericSubFrame(tk.Frame):
    __background = None
    def __init__(self, parent, background=None, **kwargs):
        super().__init__(parent, **kwargs, )
        if self.__background is None and background is None:
            self.background = parent.background
        else:
            self.background = background

    @property
    def background(self):
        return self.__background
    @background.setter
    def background(self, value):
        self.__background = value
        self.configure(background=value)

class ScrollableFrame(tk.Frame):
    __background = None
    def __init__(self, parent, background=None, **kwargs):
        if self.__background is None and background is None:
            self.__background = parent.background
            background = parent.background
        canvas = tk.Canvas(parent, background=background, **kwargs)
        scrollbar = ttk.Scrollbar(canvas, command=canvas.yview)
        canvas["yscrollcommand"] = scrollbar.set
        super().__init__(canvas, background=background, **kwargs)


