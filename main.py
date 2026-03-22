from btk.controller import Controller
from btk.labels import GenericLabel
from btk.pages import GenericPage, ColumnPage
from btk.frames import GenericSubFrame, ScrollableFrame
import tkinter.ttk as ttk
import tkinter as tk


class FirstPage(GenericPage):
    background = "green"
    def page_content(self):
        self.newbeck = GenericSubFrame(self)
        self.textual = GenericLabel(self.newbeck, text="First Page")
        self.textual.pack()
        ttk.Button(self.newbeck, text="Тык", command=lambda: self.controller.show_frame(SecondPage)).pack()
        ttk.Button(self.newbeck, text="Тык 2", command=lambda: self.my_command()).pack()
        self.newbeck.pack(ipadx=50, ipady=50)

    def my_command(self):
        self.textual.text = "Письки"
        self.textual.background = "red"
        self.newbeck.background = "red"

class SecondPage(ColumnPage):
    background = "red"
    equal_column = True
    column_count = 2
    fill_y = True
    def page_content(self):
        left_frame = GenericSubFrame(self, background="white")
        right_frame = GenericSubFrame(self, background="green")
        GenericLabel(left_frame, text="Первый").pack()
        GenericLabel(right_frame, text="Класс").pack()
        left_frame.grid(row=0, column=0, sticky="nsew")
        right_frame.grid(row=0, column=1, sticky="nsew")




class MainApp(Controller):
    title_page = "Пупа и лупа"
    height = 250
    width = 250
    preloaded_pages = [FirstPage, SecondPage]
    start_page = FirstPage



main = MainApp()
main.mainloop()