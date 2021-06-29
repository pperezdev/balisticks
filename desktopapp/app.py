import tkinter as tk
from tkhtmlview import HTMLLabel
import config

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.setTitle("home")
        self.resize(400, 400, 400, 400)
        self.create_widgets()

    def resize(self, x, y, xmax, ymax):
        self.master.geometry(f"{x}x{y}")
        self.master.minsize(x, y)
        self.master.maxsize(xmax, ymax)

    def setTitle(self, title):
        root.title(f"{config.APP_NAME} - {title}")

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

if __name__ == '__main__':
    root = tk.Tk()
    master = Application(master=root)
    master.mainloop()