# importing tkinter module
from tkinter import *
from tkinter.ttk import *  # Progressbar
from listWindow import listWindowClass
from payWindow import payWindowClass
from worstWindow import worstWindowClass
import pickle
filename = 'betalinger.pk'
infile = open(filename,'rb')
fodboldtur = pickle.load(infile)

class mainWindow:
    def __init__(self):
        self.total = 12500
        self.target = 25000

        # creating tkinter window
        self.root = Tk()
        self.root.title("Fodboldtur 2024")
        self.root.geometry("600x400")

        # TEXT
        velkomst = Label(self.root, text="Fodboldtur 2024", font=("Arial", 24))
        velkomst.pack(pady=10)

        # Progress bar widget
        self.progressLabelText = StringVar()
        self.progressLabelText.set(f"{self.total} / {self.target} Indsamlet")

        self.progressLabel = Label(self.root, textvariable=self.progressLabelText, font=("Arial", 16))
        self.progressLabel.pack()

        self.progress = Progressbar(self.root, orient=HORIZONTAL, length=200, mode='determinate')
        self.progress['value'] = (self.total / self.target) * 100
        self.progress.pack(pady=10)

        # Input frame for entry widgets and buttons
        input_frame = Frame(self.root)
        input_frame.pack(pady=10)

        # Buttons
        self.button1 = Button(input_frame, text="Indbetal", command = lambda: payWindowClass(self))
        self.button1.pack(side=LEFT, padx=5)

        self.button2 = Button(input_frame, text="Liste over betalinger", command = lambda: listWindowClass(self))
        self.button2.pack(side=LEFT, padx=5)


        # Top 3 brookies section
        brookies_label = Label(self.root, text="Top 3 brookies", font=("Arial", 20))
        brookies_label.pack(pady=10)

        self.brookie_1 = Label(self.root, text="Nummer 1 - 1200/4500", font=("Arial", 14))
        self.brookie_1.pack()

        self.brookie_2 = Label(self.root, text="Nummer 2 - 1500/4500", font=("Arial", 14))
        self.brookie_2.pack()

        self.brookie_3 = Label(self.root, text="Nummer 3 - 2000/4500", font=("Arial", 14))
        self.brookie_3.pack()

        # infinite loop
        mainloop()


if __name__ == '__main__':
    main = mainWindow()
