#!/usr/bin/env python3

import tkinter as tk
import math

# from tkinter import ttk


class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if "textvariable" not in kw:
            self.variable = tk.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kw["textvariable"]

    @property
    def value(self):
        return self.variable.get()

    @value.setter
    def value(self, new: str):
        self.variable.set(new)


class Application(tk.Tk):
    name = "Foo"
    title_ = "Reverse calculator"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.title_)
        self.bind("<Escape>", self.quit)
        self.entry = MyEntry(self)
        self.entry.pack()
        self.listbox = tk.Listbox(self)
        self.listbox.pack()

        self.entry.bind("<Return>", self.process)
        self.entry.bind("<KP_Enter>", self.process)

    def process(self, e: tk.Event):
        values = self.entry.value.split()
        for value in values:
            if value in ["+","-","*","/","//","**","%"]:
                num1 = self.listbox.get(0)
                num2 = self.listbox.get(1)
                res = eval(f"{num1} {value} {num2}")
                self.listbox.delete(0, 1)
                self.listbox.insert(0, res)
            elif value.isalnum():
                self.listbox.insert(self.listbox.index("end"), value)
            else:
                self.entry.value = "INVALID INPUT"
            self.entry.value = ""

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
