from tkinter import Text
from tkinter import Scrollbar
from tkinter import LEFT, RIGHT, BOTH, END, Y

from menu import ToolBar
from functions import set_bg_colors

"""
    file containing the window codebase
"""

class Window:
    """main window"""
    def __init__(self, app):
        """constructor"""
        self.app = app # declaring reference to the main tkinter instance
        self.app.title("Coddict") # assign "coddict" to the window title
        self.app.geometry("1100x600+100+20") # assign the window dimensions
        self.app.state("zoomed") # maximize window
        self.app.iconbitmap("icon.ico") # set window icon
        police = ('ubuntu', 12) # declare font-style class attribute with ubuntu style and 12 size

        #----------------------attributes------------------------------
        self.text_zone = Text(self.app, font=police) # create text area
        self.scroll_zone = Scrollbar(self.app, command=self.text_zone.yview) # create scrollbar

        # configure text area
        self.text_zone.config(yscrollcommand=self.scroll_zone.set, bg="#1E1E1E", fg="#FFFFFF", insertbackground="#FFFFFF") # set background color to dark

        self.tools = ToolBar(self) # create tools bar
        
        #----------------------colors-designs---------------------------

        #----------------------positions--------------------------------
        self.text_zone.pack(side=LEFT, fill=BOTH, expand=True) # positioning text widget in the left side
        self.scroll_zone.pack(side=RIGHT, fill=Y) # positioning scrollbar in the right side
