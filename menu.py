from tkinter import Menu
import window

"""
file containing the menuBar codebase
"""

class ToolBar:
    """tool-bar class"""

    def __init__(self, mother_class):
        """constructor"""
        self.menu = Menu(mother_class.app)
        mother_class.app.configure(menu=self.menu)

        #-------------------tools---------------------
        file = Menu(self.menu, tearoff=False)
        file.add_command(label="New", command=mother_class.create)
        file.add_command(label="Open", command=mother_class.fopen)
        file.add_command(label="Save", command=mother_class.save_file)
        file.add_command(label="Save as", command=mother_class.save_as_file)
        file.add_command(label="Exit", command=exit)

        self.menu.add_cascade(label="File", menu=file)
