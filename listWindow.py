from PIL import ImageTk, Image  # image stuff - install package: Pillow
from tkinter import *

class listWindowClass:
    def __init__(self, master):
        self.master = master  # reference to main window object
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")

        # Top frame spanning the entire width
        self.topFrame = Frame(self.listWindow, borderwidth=2, relief=GROOVE)
        self.topFrame.pack(side=TOP, fill=X)
        Label(self.topFrame, text="Liste over alle fodboldturens deltagere,", font=('Arial 15 bold')).pack(side=LEFT, pady=(0,10) )

        # Left frame
        self.leftFrame = Frame(self.listWindow, borderwidth=2, relief=GROOVE)
        self.leftFrame.pack(side=LEFT, fill=BOTH, expand=False)  # Changed expand to False
        for item in self.master.fodboldtur:
            Label(self.leftFrame, text=item).pack(side=TOP, anchor='w', padx=(0,15))  # Align labels to the left

        # right frame
        self.rightFrame = Frame(self.listWindow, borderwidth=2, relief=GROOVE)
        self.rightFrame.pack(side=RIGHT, fill=BOTH, expand=True)
        #for keys in self.master.fodboldtur.keys():
         #   self.progress = Progressbar(self.root, orient=HORIZONTAL, length=200, mode='determinate')
          #  self.progress['value'] = (self.master.fodboldtur.keys() / self.master.personaltarget) * 100
           # self.progress.pack(pady=10)

        # middle frame
        self.middleFrame = Frame(self.listWindow, borderwidth=2, relief=GROOVE)
        self.middleFrame.pack(fill=BOTH, expand=True)
        for key in self.master.fodboldtur.keys():
            Label(self.middleFrame, text=f'{self.master.fodboldtur[key]} / {self.master.personaltarget}').pack(side=TOP, anchor='w')  # Align labels to the center


# Example to show how to use this class
# root = Tk()
# my_gui = listWindowClass(root)
# root.mainloop()
