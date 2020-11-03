#usr/bin/python3
from tkinter import Tk
from window import Window

# Coddict is a simple text editor for python developers.

if __name__ == "__main__":
    app = Tk() # create Tk instance 'the main application'
    w = Window(app) # define a window from app
    app.mainloop() # turn an infinite loop


# Created by: karim bahri
# Project starting: 30/09/2020