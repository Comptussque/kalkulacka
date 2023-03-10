import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "gui.ui"


class Application:
    def __init__(self, master=None):
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object("mainWindow", master)
        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def up(self):
        pass

    def down(self):
        pass

    def delete(self):
        pass

    def quit(self):
        self.mainwindow.quit()


if __name__ == "__main__":
    app = Application()
    app.run()
