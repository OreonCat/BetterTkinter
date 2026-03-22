import tkinter as tk

class GenericLabel(tk.Label):
    __background = None
    __font_size = None
    __font_family = None
    __font_weight = None
    __text = None
    def __init__(self, parent, text="", background=None, font_size=12, font_family="black", font_weight="", **kwargs):
        if background is None and self.__background is None:
            print(parent.background)
            self.__background = parent.background
            background = parent.background
        self.__text = text
        self.__font_size = font_size
        self.__font_family = font_family
        self.__font_weight = font_weight
        super().__init__(parent, **kwargs, text=text, background=background, font=(font_family, font_size, font_weight))

    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, value):
        self.__background = value
        self.configure(background=value)

    @property
    def font_size(self):
        return self.__font_size

    @font_size.setter
    def font_size(self, value):
        self.__font_size = value
        self.configure(font=(self.__font_family, self.__font_size, self.__font_weight))

    @property
    def font_family(self):
        return self.__font_family

    @font_family.setter
    def font_family(self, value):
        self.__font_family = value
        self.configure(font=(self.__font_family, self.__font_size, self.__font_weight))

    @property
    def font_weight(self):
        return self.__font_weight

    @font_weight.setter
    def font_weight(self, value):
        self.__font_weight = value
        self.configure(font=(self.__font_family, self.__font_size, self.__font_weight))

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value
        self.configure(text=value)