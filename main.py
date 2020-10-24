from tkinter import Tk
from window import Window

if __name__ == "__main__":
    app = Tk()
    app.configure(bg="#1E1E1E")
    w = Window(app)
    app.mainloop()
