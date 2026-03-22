import tkinter as tk
from email.encoders import encode_quopri
from tkinter import ttk, Widget
from tkinter.ttk import Frame


class GenericPage(tk.Frame):
    background = None
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, **kwargs, background=self.background)
        self.controller = controller
        self.page_content()

    def page_content(self):
        pass

class ColumnPage(GenericPage):
    equal_column = True
    column_count = 0
    fill_y = False
    not_equal_column_weight = []

    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, controller, **kwargs)

        if self.equal_column:
            for i in range(0, self.column_count):
                self.columnconfigure(i, weight=1)
        else:
            count = 0
            for weight in self.not_equal_column_weight:
                self.columnconfigure(count, weight=weight)
                count += 1

        if self.fill_y:
            self.rowconfigure(0, weight=1)
