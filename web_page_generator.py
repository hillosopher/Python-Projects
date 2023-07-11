import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        # window
        Frame.__init__(self,master)
        self.master.title("Web Page Generator")
        self.master.resizable(False,False)


        # interface elements
        self.entryText = StringVar()
        self.label = Label(self.master, text="Enter custom text or click the DefaultHTML page button")
        self.entry = Entry(self.master, textvariable=self.entryText, width=120)
        self.btnFrame = Frame(self.master)# create frame for buttons to pack at bottom of interface
        self.btnDefault = Button(self.btnFrame, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btnCustom = Button(self.btnFrame, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        
        # elements' layout
        self.label.grid(column=0, row=0, padx=5, pady=5, sticky=W)
        self.entry.grid(column=0, row=1, columnspan=2, padx=5, pady=5, sticky=W)
        
        # place buttons inside the frame
        self.btnDefault.pack(side=LEFT, padx=5)
        self.btnCustom.pack(side=LEFT, padx=5)
        
        # position the frame in the grid
        self.btnFrame.grid(column=1, row=2, pady=5, sticky=E)

    def openTab(self, text):
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + text + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def defaultHTML(self):
        text = "Stay tuned for our amazing summer sale!"
        self.openTab(text)
        
    def customHTML(self):
        text = self.entryText.get()
        self.openTab(text)
        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
