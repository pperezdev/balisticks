import tkinter as tk
from tkhtmlview import HTMLLabel
import config

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.setTitle("home")

        self.bind("<Configure>", self.resize)

        self.defineGeometry(400, 400, 400, 400)
        self.create_widgets()

    def defineGeometry(self, width, height, width_max, height_max):
        self.width = width
        self.height = height
        self.width_max = width_max
        self.height_max = height_max

        self.master.geometry(f"{self.width}x{self.height}")
        self.master.minsize(self.width, self.height)
        self.master.maxsize(self.width_max, self.height_max)

    def setTitle(self, title):
        root.title(f"{config.APP_NAME} - {title}")

    def create_widgets(self):
        self.frame_left = tk.Frame(self, width=self.width*0.25, height=self.height, bg="red")
        self.frame_left.grid(row=0, column=0)

        self.frame_center = tk.Frame(self, width=self.width*0.75, height=self.height, bg="blue")
        self.frame_center.grid(row=0, column=1)

        #self.hi_there = tk.Button(self)
        #self.hi_there["text"] = "Hello World\n(click me)"
        #self.hi_there["command"] = self.say_hi
        #self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)

    def resize(self, event):
        ...

if __name__ == '__main__':
    root = tk.Tk()
    master = Application(master=root)
    master.mainloop()