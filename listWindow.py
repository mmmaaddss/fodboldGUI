from PIL import ImageTk, Image  # image stuff - install package: Pillow
from tkinter import *
import pickle
filename = 'betalinger.pk'
infile = open(filename,'rb')
fodboldtur = pickle.load(infile)

class listWindowClass:
    def __init__(self, master):
        self.master = master  # reference to main window object
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")

        # Top frame spanning the entire width
        self.topFrame = Frame(self.listWindow)
        self.topFrame.pack(side=TOP, fill=X)
        Label(self.topFrame, text="Liste over alle fodboldturens deltagere,", font=("Arial", 15)).pack(side=LEFT, pady=(0,10) )

        # Left frame
        self.leftFrame = Frame(self.listWindow)
        self.leftFrame.pack(side=LEFT, fill=BOTH, expand=False)  # Changed expand to False
        for item in fodboldtur:
            Label(self.leftFrame, text=item).pack(side=TOP, anchor='w')  # Align labels to the left

        # Right frame
        self.rightFrame = Frame(self.listWindow)
        self.rightFrame.pack(side=RIGHT, fill=BOTH, expand=True)
        for item in fodboldtur:
            Label(self.rightFrame, text=item[1]).pack(side=TOP, anchor='w')  # Align labels to the right

        # Example of how you might use the left and right frames
        # Label(self.leftFrame, text="Left Frame Content").pack()
        # Label(self.rightFrame, text="Right Frame Content").pack()

# Example to show how to use this class
# root = Tk()
# my_gui = listWindowClass(root)
# root.mainloop()
