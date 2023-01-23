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
        self.listbox = tk.Listbox(self, selectmode="multiple")
        self.listbox.pack()
        # Error messageP
        self.errorStr = tk.StringVar()
        self.error_info = tk.Label(self, textvariable=self.errorStr)
        self.error_info.pack()

        # Buttons
        button_width = 15
        self.button_delete = tk.Button(self, width=button_width, text="DELETE", command=self.delete)
        self.button_clear = tk.Button(self, width=button_width, text="CLEAR", command=self.clear)
        self.button_copy = tk.Button(self, width=button_width, text="COPY", command=self.copy)
        self.button_move_up = tk.Button(
            self, text="MOVE UP", width=button_width, command=self.move_up)
        self.button_move_down = tk.Button(
            self, text="MOVE DOWN", width=button_width, command=self.move_down)

        self.button_delete.pack()
        self.button_clear.pack()
        self.button_copy.pack()
        self.button_move_up.pack()
        self.button_move_down.pack()

        self.entry.bind("<Return>", self.process)
        self.entry.bind("<KP_Enter>", self.process)

        # Dict   ||key: operator     value: amount of operands||
        self.operators = {
            # 2 operator funcs
            "+":    2,
            "-":    2,
            "*":    2,
            "/":    2,
            "**":   2,
            "//":   2,
            "%":    2,
            # 1 operator funcs
            "sin":  1,
            "cos":  1,
            "tan":  1,
            "log":  1,
            "log2": 1,
            # consts (key = name     value = value)
            "pi": 3.1415
        }

    def process(self, e: tk.Event):
        _input = self.entry.value.lower().split()
        self.errorStr.set("")
        # check for operators
        for value in _input:
            if value in self.operators.keys():
                # check if enough operands
                if self.operators[value] == 2:
                    try:
                        num1 = self.listbox.get(0)
                        num2 = self.listbox.get(1)
                        res = eval(f"{num1} {value} {num2}")
                        self.listbox.delete(0, 1)
                    except:
                        self.errorStr.set("Not enough operands!")
                        break
                elif self.operators[value] == 1:
                    num1 = self.listbox.get(0)
                    res = eval(f"math.{value}({num1})")
                    self.listbox.delete(0)
                # if not operator but const
                else:
                    res = self.operators[value]
                self.listbox.insert(0, res)
            else:
                # check if value is number
                try:
                    value = float(value)
                    self.listbox.insert(self.listbox.index("end"), value)
                except:
                    self.errorStr.set("Invalid input!")
            self.entry.value = ""

    # Button functions
    def delete(self):
            for select_index in self.listbox.curselection():
                self.listbox.delete(select_index)
    def copy(self):
        pass
    def clear(self):
        self.listbox.delete(0, self.listbox.size())
    def move_up(self):
        for select_index in self.listbox.curselection():
            select = self.listbox.get(select_index)
            self.listbox.delete(select_index)
            self.listbox.insert(select_index-1, select)

    def move_down(self):
        for select_index in self.listbox.curselection():
            select = self.listbox.get(select_index)
            self.listbox.delete(select_index)
            self.listbox.insert(select_index+1, select)

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
