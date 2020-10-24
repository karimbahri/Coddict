from tkinter import Text
from tkinter import Scrollbar
from tkinter import LEFT, RIGHT, BOTH, END, Y
from tkinter.filedialog import askopenfilename as ask_file
from tkinter.filedialog import asksaveasfilename as ask_save

from menu import ToolBar
#from functions import set_bg_colors

"""
    file containing the window codebase
"""

class Window:
    """main window"""
    def __init__(self, app):
        """constructor"""
        self.path = ""
        self.pos = 1.0
        self.app = app
        self.app.title("Coddict")
        self.app.geometry("1100x600+100+20")
        self.app.state("zoomed")
        self.app.iconbitmap("icon.ico")
        police = ('ubuntu', 12)

        #----------------------attributes------------------------------
        self.text_zone = Text(self.app, font=police)
        self.scroll_zone = Scrollbar(self.app, command=self.text_zone.yview)

        self.text_zone.config(yscrollcommand=self.scroll_zone.set, bg="#1E1E1E", fg="#FFFFFF")
        self.text_zone.tag_configure("red", foreground="red")
        
        self.tools = ToolBar(self)
        
        #----------------------colors-designs---------------------------

        #----------------------positions--------------------------------
        self.text_zone.pack(side=LEFT, fill=BOTH, expand=True)
        self.scroll_zone.pack(side=RIGHT, fill=Y)

    def create(self):
        """create new file"""
        self.text_zone.delete(self.pos, END)

    def fopen(self):
        """open file"""
        types = [("All Files", "*.*")]
        self.path = ask_file(defaultextension=".py", filetypes=types)
        if len(self.path):
            self.text_zone.delete(self.pos, END)
            with open(self.path, "r") as file:
                content = file.read()
                self.text_zone.insert(self.pos, content)

    def save_file(self):
        """save file method"""
        if self.path:
            content = self.text_zone.get(self.pos, END)
            with open(self.path, "w") as file:
                file.write(content)
        else:
            self.save_as_file()

    def save_as_file(self):
        """save as file method"""
        types = [("All Files", "*.*")]
        self.path = ask_save(filetypes=types)
        content = self.text_zone.get(self.pos, END)
        with open(self.path, "w") as file:
            file.write(content)
