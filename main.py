from btk.controller import Controller
from btk.pages import GenericPage
import tkinter.ttk as ttk
import tkinter as tk


class FirstPage(GenericPage):
    background = "red"
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        tk.Label(self, text="Ну что епта").pack()
        ttk.Button(self, text="Тык", command=lambda: controller.show_frame(SecondPage)).pack()

class SecondPage(GenericPage):
    background = "green"
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        tk.Label(self, text="Ды ды ды").pack()

class MainApp(Controller):
    title_page = "Пупа и лупа"
    height = 250
    width = 250
    preloaded_pages = [FirstPage, SecondPage]
    start_page = FirstPage



main = MainApp()
main.mainloop()