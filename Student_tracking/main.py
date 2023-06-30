# to do:
# - Figure out how to retrieve information from entry fields to add to database with query


import tkinter as tk
from tkinter import * 
from database import addStudent

class ParentWindow(Frame):
    def addStudent(self):
                first_name = self.fname.get()
                last_name = self.lname.get()
                phone_num = self.phone.get()
                email_add = self.email.get()
                cur_course = self.course.get()

                addStudent(first_name, last_name, phone_num, email_add, cur_course)

    def __init__(self, master):
        Frame.__init__(self, master)

# open window and create its dimensions, bg color, and title
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('1000x500')
        self.master.title('Student Tracking App')
        self.master.config(bg='#8DF9C8')

# declaring Entry text as String Var as to retrieve it with the .get method later
        self.fname = StringVar()
        self.lname = StringVar()
        self.phone = StringVar()
        self.email = StringVar()
        self.course = StringVar()

# labels for the Entry fields on the form
        self.lblfname = Label(self.master, text='First Name',font='helvetica 20', bg='#8DF9C8')
        self.lblfname.grid(column='0', row='1', padx=(30,0), pady=(30,0))
        self.lbllname = Label(self.master, text='Last Name',font='helvetica 20', bg='#8DF9C8')
        self.lbllname.grid(column='0', row='3', padx=(30,0), pady=(30,0))
        self.lblphone = Label(self.master, text='Phone',font='helvetica 20', bg='#8DF9C8')
        self.lblphone.grid(column='0', row='5', padx=(30,0), pady=(30,0))
        self.lblemail = Label(self.master, text='Email Address',font='helvetica 20', bg='#8DF9C8')
        self.lblemail.grid(column='0', row='7', padx=(30,0), pady=(30,0))
        self.lblcourse = Label(self.master, text='Current Course',font='helvetica 20', bg='#8DF9C8')
        self.lblcourse.grid(column='0', row='9', padx=(30,0), pady=(30,0))

# Entry fields on the form
        self.txtfname = Entry(self.master, textvariable=self.fname, font='helvetica 16', bg='white')
        self.txtfname.grid(column='1', row='1', padx=(30,0), pady=(30,0), columnspan=2)
        self.txtlname = Entry(self.master, textvariable=self.lname, font='helvetica 16', bg='white')
        self.txtlname.grid(column='1', row='3', padx=(30,0), pady=(30,0), columnspan=2)
        self.txtphone = Entry(self.master, textvariable=self.phone, font='helvetica 16', bg='white')
        self.txtphone.grid(column='1', row='5', padx=(30,0), pady=(30,0), columnspan=2)
        self.txtemail = Entry(self.master, textvariable=self.email, font='helvetica 16', bg='white')
        self.txtemail.grid(column='1', row='7', padx=(30,0), pady=(30,0), columnspan=2)
        self.txtcourse = Entry(self.master, textvariable=self.course, font='helvetica 16', bg='white')
        self.txtcourse.grid(column='1', row='9', padx=(30,0), pady=(30,0), columnspan=2)
        

# Listbox
        self.listbox = Listbox(self.master, font='helvetica 12', bg='white')
        self.listbox.grid(column='3', row='3', padx=(30,0), pady=(0,0), sticky=(N, E))

#buttons
        self.addbtn = Button(self.master, font='helvetica 12', command=self.addStudent, text='Add Student')
        self.addbtn.grid(column='3', row='5')
        self.removebtn = Button(self.master, font='helvetica 12', command='#', text='Remove Student')
        self.removebtn.grid(column='4', row='5') 





if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
