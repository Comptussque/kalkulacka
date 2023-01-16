#!/usr/bin/env python3

import tkinter as tk

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
        print(self.entry.value)
        self.entry.value = ""

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
