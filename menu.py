from tkinter import Menu
from subprocess import call
from tkinter.filedialog import askopenfilename as ask_file
from tkinter.filedialog import asksaveasfilename as ask_save
from tkinter import messagebox
from tkinter import LEFT, RIGHT, BOTH, END, Y
"""
file containing the menuBar codebase
"""
class ToolBar:
    """tool-bar class"""

    def __init__(self, mother_class):
        """constructor"""
        self.menu = Menu(mother_class.app) # create menu bar
        mother_class.app.configure(menu=self.menu) # add menu bar to window
        self.state = False # declaring boolean with the value False
        # assigning state False value to avoid the execution of the script
        # automatically.

        self.path = "" # declaring empty string for file path
        self.pos = 1.0 # declaring text widget position to the beginning of the text field
        #-------------------tools---------------------
        file = Menu(self.menu, tearoff=False) # create sub-menu for fileManagement
        file.add_command(label="New", command=self.create) # add newFile command to the submenu
        file.add_command(label="Open", command=self.fopen) # add openFile command to the submenu
        file.add_command(label="Save", command=self.save_file) # add saveFile command to the submenu
        file.add_command(label="Save as", command=self.save_as_file) # add saveAsFile command to the submenu
        file.add_command(label="Exit", command=exit) # add exit to the submeni

        run = Menu(self.menu, tearoff=False) # create sub-menu for script execution
        run.add_command(label="Execute", command=self.execute) # add executeFile to the submenu

        self.menu.add_cascade(label="File", menu=file) # add file submenu to menu bar
        self.menu.add_cascade(label="Run", menu=run) # add run submenu to menu bar

        self.state = True # assign state bool True value
        self.window = mother_class # declaring reference to window instance

    # execute method:
    # method used to execute script written with python
    # it is executed only if state is True
    def execute(self):
        if self.state:
            # test if path is not empty to execute script
            # otherwise it shows error message
            if not len(self.path):
                messagebox.showerror("No file to execute")
            else:
                call(["python", self.path])

    # create method:
    # method used to create new file
    def create(self):
        """create new file"""
        # delete the containing of the text area
        self.window.text_zone.delete(self.pos, END)

    # fopen method:
    # method used to open a file
    def fopen(self):
        """open file"""
        types = [("All Files", "*.*")] # select all types of files
        self.path = ask_file(defaultextension=".py", filetypes=types) # asking for file with default
        # extension .py
        if len(self.path): # check if path is not empty
            self.window.text_zone.delete(self.pos, END) # delete the containing of the text area
            with open(self.path, "r") as file: # open the file with read-only permission
                content = file.read() # assign content the content of the file
                self.window.text_zone.insert(self.pos, content) # insert the content of the file to text area

    # save_file method:
    # method used to save existing file
    def save_file(self):
        """save file method"""
        if self.path: # check if path is not empty
            content = self.window.text_zone.get(self.pos, END) # assign the content of text area to the 
            # variable content
            with open(self.path, "w") as file: # open file with write-only permission
                file.write(content) # write the content of text area into the file
        else: #otherwise use save_as_method
            self.save_as_file()

    # save_as_file method:
    # method used to save new file
    def save_as_file(self):
        """save as file method"""
        types = [("All Files", "*.*")] # select all types of file
        self.path = ask_save(filetypes=types) # ask for saving file location
        content = self.window.text_zone.get(self.pos, END) # assign content the text area content
        with open(self.path, "w") as file: # open the file with write-only permission
            file.write(content) # write the content of text area into the file
